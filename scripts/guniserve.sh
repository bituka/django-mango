#!/bin/bash
set -e
LOGFILE=/home/mango/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=mango
# GROUP=pypug
ADDRESS=unix:/tmp/gunicorn.sock
cd /home/mango/django-mango/mango
source /home/mango/mangoenv/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn mango.wsgi:application -w $NUM_WORKERS --bind=$ADDRESS \
  --user=$USER --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE