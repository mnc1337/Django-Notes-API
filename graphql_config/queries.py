import graphene
from graphql import GraphQLError
from .types import UserType, NoteType
from notes_api_app.models import Note
from graphql_jwt.decorators import login_required


class Query(graphene.ObjectType):
    me = graphene.Field(UserType)
    note = graphene.Field(
        NoteType,
        title=graphene.String(required=False),
        uuid=graphene.String(required=False),
    )
    notes = graphene.List(NoteType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

    @login_required
    def resolve_note(root, info, title=None, uuid=None):
        if title is None and uuid is None:
            raise GraphQLError("Either title or UUID of note should be provided!")

        if title is not None and uuid is None:
            note = Note.objects.filter(title=title).first()
        elif title is None and uuid is not None:
            note = Note.objects.filter(uuid=uuid).first()
        else:
            note = Note.objects.filter(title=title, uuid=uuid).first()

        return note

    @login_required
    def resolve_notes(root, info):
        return Note.objects.all()
