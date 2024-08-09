# NameGenerator initialization
#
#

HOST=0.0.0.0
NAME_DATABASE_PORT=5500
NAME_DATABASE=NameGeneratorDB

echo "Creating NameGenerator tables"
mysql -h $HOST -P $NAME_DATABASE_PORT -u "$1" --password="$2" $NAME_DATABASE < ./queries/main.sql

