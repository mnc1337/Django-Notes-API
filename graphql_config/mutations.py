import graphene
from .types import UserType, NoteType
from notes_api_app.models import User, Note
from graphql_jwt.decorators import login_required
from graphql import GraphQLError


class CreateNote(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String()
        is_important = graphene.Boolean()

    note = graphene.Field(NoteType)
    ok = graphene.Boolean()

    @login_required
    def mutate(root, info, title, content=None, is_important=False):
        user = info.context.user
        note = Note.objects.create(
            title=title, content=content, is_important=is_important, user=user
        )

        return CreateNote(note=note, ok=True)


class UpdateNote(graphene.Mutation):
    class Arguments:
        uuid = graphene.UUID(required=True)
        title = graphene.String()
        content = graphene.String()
        is_important = graphene.Boolean()

    note = graphene.Field(NoteType)
    ok = graphene.Boolean()

    @login_required
    def mutate(root, info, uuid, **kwargs):
        user = info.context.user
        note = Note.objects.filter(uuid=uuid, user=user).first()

        if not note:
            raise GraphQLError(
                "Note not found. Perhaps it was deleted or you don't have a permission?"
            )

        readonly_fields = {"uuid", "id", "created_at", "updated_at", "user"}

        for key, value in kwargs.items():
            if key not in readonly_fields:
                setattr(note, key, value)

        note.full_clean()
        note.save()

        return UpdateNote(note=note, ok=True)


class DeleteNote(graphene.Mutation):
    class Arguments:
        uuid = graphene.UUID(required=True)
        title = graphene.String()

    deleted_note_uuid = graphene.UUID()
    ok = graphene.Boolean()

    @login_required
    def mutate(root, info, uuid, title=None):
        user = info.context.user
        filters = {"uuid": uuid, "user": user}

        if title:
            filters["title"] = title

        note = Note.objects.filter(**filters).first()

        if not note:
            raise GraphQLError(
                "Note not found. Perhaps it was deleted or you don't have a permission?"
            )

        note.delete()

        return DeleteNote(deleted_note_uuid=uuid, ok=True)


class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()
    update_note = UpdateNote.Field()
    delete_note = DeleteNote.Field()
