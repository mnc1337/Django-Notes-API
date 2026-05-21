# Django-Notes-API

---

## Some words about project
It's important to keep your notes at secure and understandable place. 
**Notes API** project is meant to manage your notes in simple way. 
You can manage notes via Django Admin Panel (is you are staff with some permissions or superuser), REST Framework and GraphQL implementing CRUD operations template: 
    - creating;
    - reading;
    - updating;
    - deleting.

---

## Project vocabulary
**API** - Application Programming Interface: a set of rules and protocols that allows some different software applications to communicate and share data with each other.
**REST Framework** - a collection of tools, libraries, and pre-written code that helps developers easily build RESTful APIs.
**GraphQL** - an open-source query language for APIs and a runtime for fulfilling those queries with your existing data.

---

## How to use API
This API (Application Programming Interface) is simple in using. The main concept consists of the following: you (client) deal with database (server). Notes are stored in database and only **you** know content of **your** notes. Nobody else can access your notes and read information stored there. 
When you visit API for the first time, you will see a main page and some blocks; by selecting one of them, you'll be able to perform different actions. 
List of actions: 
    - **Log in to your account** - sign in to account (if you already have one);
    - **Create a user** - create a user (and automatical logging in);
    - **Create a note (via REST Framework)** - create a note using REST Framework (it works only for users that are logged in; if you are logged out, you will get a 403 error, because you don't have necessary permissions);
    - **Create a note (via GraphQL)** - create a note using GraphQL (you'll be able to perform CRUD operations, but you won't get information that you looked for);
    - **See all REST Framework endpoints** - check all REST framework endpoints using Swagger API (other external API for easier browsing of available URLs);
    - **Go to home page of app** - go to home page of app - technical part of project (it doesn't have any other endpoints, but is crucial for valid functioning of project).

---

## Security

There is a `_security` folder in project structure. It contains an archive with a nested archive and an `.asc` file - digital signature. **To check archive originality**, you can download archive, extract nested archive (`.7z`) and `.asc` file from it to directory **selected by you** and use there the next command in Bash/WSL console: `gpg --verify webprograms_archive.7z.asc webprograms_archive.7z` - first parameter is a digital signature (`.asc` file), second parameter is an archive.

---

## License

This project is licensed under the MIT license. See the `LICENSE` file in root directory for details.

---

*2026, author: mnc1337*