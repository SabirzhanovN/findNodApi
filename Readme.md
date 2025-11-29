git clone https://github.com/SabirzhanovN/findNodApi.git
cd findNodApi

python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver