# SQL demonstration in Python

This project is part of a [social media app](https://github.com/0xd5dc/microservice-go), which allows users to invite people to their events with a chat feature,
demonstrates communications with SQL database using SQLalchemy, which is the most sufficient library I can use to
function like my original Go-lang code. However,Python doesn't have a modern feature like map() in Go-lang.
Consequently, Python object and JSON object conversion needs to be implemented individually. Moreover, database create,
read, update, delete(CRUD) functions have to define specifically for each field(s) mutation.

### Model: Database schema

- User: users
    - user_id
    - name
    - password
    - phone
    - email
    - token
    - email_confirmed
    - created_at
    - updated_at
    - deleted_at
- Event: events
    - event_id
    - name
    - detail
    - owner_id
    - is_virtual
    - is_private
    - created_at
    - updated_at
    - deleted_at
    - start_at
    - end_at
- Guest: guests
    - guest_id
    - user_id
    - event_id

## Design

- db.py
    - User(Base), Event(Base), Guest(Base), defines the data models
    - DataAccessLayer() defines a utility to communicate with database
        - connect()
            - starts a session with database
- db_seeder.py
    - user_seeder(size: int)
        - generated a list of user objects with a specific size input
    - event_seeder(size: int, user_size: int)
        - generated a list of event objects with a specific size input
    - guest_seeder(size: int, user_size: int, event_size: int)
        - generated a list of guest objects with a specific size input
    - run_seeder(session, user_size: int, event_size: int, guest_size: int)
        - runs all seeders to populate the database
- app.py
    - create_user(session, user)
        - create a user
    - create_event(session, event)
        - create an event
    - read_users(session)
        - read_users gets all users in the database
    - read_events(session)
        - read_events gets all events in the database
    - update_user_name_by_email(session, email, name)
        - update username by its email
    - update_event_detail_by_name(session, name, detail)
        - update event detail by event name
    - delete_user_by_email(session, email)
        - delete user by email
    - delete_event_by_name(session, name)
        - delete event by name

## Plan & Implement

- [x] migration
- [x] seeder using faker
- [x] read users
- [x] create user
- [x] update user
- [x] delete user
- [x] read events
- [x] create event
- [x] update event
- [x] delete event
- [ ] get guest list by event id
- optional
- [ ] seeder factory pattern to extract data from files
- [ ] parse into objects

## Tests

- [x] migration
- [x] seeder
- [x] read users
- [x] create user
- [x] update user
- [x] delete user
- [x] read events
- [x] create event
- [x] update event
- [x] delete event
- [ ] get guest list

## Issues & Fixes

- [x] os path causes tests use different local db file fixed by using in-memory db in unit-tests
- [ ] SQLalchemy doesn't couple/decouple data automatically like Go-lang
- [ ] RETURNING is not supported by this dialect's statement compiler, sqlite.
- [ ] insert or update feature not available in sqlite