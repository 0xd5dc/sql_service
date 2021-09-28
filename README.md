# SQL code adaptatiton of Go-lang project

### Model

- User
- Event
- Guest

## files

- db.py
- db_seeder.py

## plan & implement

- [x] migration
- [x] seeder using faker
- [x] read users
- [x] create user
- [x] update user
- [x] delete user
- [ ] read events
- [ ] create event
- [ ] update event
- [ ] delete event
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

- [ ] curd events
- [ ] get guest list

## issues
- [ ] os path causes tests use different local db file 
- [ ] SQLalchemy doesn't couple/decouple data automatically like Go-lang