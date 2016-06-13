# Desaga

Desaga does virtual lab management for practical technical training.

- Instructors create labs
- Students register
- Desaga provisions virtual infrastructure for each student

Behind the scenes it uses

- Django
- Celery (future)
- Docker (work in progress)
- OpenStack Nova and HEAT (future)

## What's up with the name?

The Bunsen burner wasn't created by Bunsen alone.  His assistant,
Peter Desaga, helped develop the burner.  Sir Martyn Poliakoff points
out that no one remembers Bunsen's assistant's name.  When asked the
name, Poliakoff admits that he doesn't remember either.  See for yourself:
[Bunsen Burner by Periodic Videos](https://youtu.be/ZmtbMKJLUJo?t=1m50s)

This application is a lab assistant that should work in the background
mostly unnoticed, so the name seems to fit.
