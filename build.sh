#!/usr/bin/env bash
set -o errexit

package manager (pip, poetry, etc.)
pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate