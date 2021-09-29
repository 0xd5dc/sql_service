# SQL code adaptatiton of Go-lang project

### Model

- User
- Event
- Guest

## files

- db.py
- db_seeder.py
- repo.py

## plan & implement

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

## tests

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

## issues & fixes
- [x] os path causes tests use different local db file fixed by using in-memory db in unit-tests
- [ ] SQLalchemy doesn't couple/decouple data automatically like Go-lang