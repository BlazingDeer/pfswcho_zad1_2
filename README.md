PFSWCHO zadanie 1 Daniel Florek Sprawozdanie

Link github - https://github.com/BlazingDeer/pfswcho_zad

Frontend jest na http://127.0.0.1:8000/

API jest na http://api:8002/api/v1/fibseq/

BD jest na domyślnym porcie 5432 i jest połączone tylko z API, nie można się połączyć z zewnątrz.

Aplikacja składa się z trzech kontenerów: frontend, API oraz bazy danych. Frontend przedstawia interfejs
użytkownika oraz komunikuje się z API. API oblicza wartość ciągu Fibonacciego na podstawie liczby otrzymanej z
konteneru frontend i komunikuje się z postgresql BD w celu zapisania wartości (Metoda POST). W przypadku metody
GET, API zwraca ostanie 10 zapisanych wartości z bazy danych.

Frontend został napisany przy użyciu frameworka Django w języku python, a komunikacja pomiędzy frontendem a
API jest zrealizowana poprzez moduł Requests.

API również zostało wykonane w języku python przy pomocy Django oraz Django Rest Framework. Zachowuje się w
nim model bazy danych oraz kod obliczający wartość ciągu. Serializer przekłada model na obiekt json, natomiast
viewset pozwalają na komunikację CRUD API z frontendem. Połączenie z DB jest automatycznie wykonywane przez
Django przy podaniu odpowiednich ustawień dla projektu.

Baza danych jest kontenerem Dockera i oprócz hasła i nazwy użytkownika nic nie zostało zmienione.
Wszystkie kontenery są połączone poprzez docker-compose i są uruchamiane poprzez polecenie:
docker-compose up -d --build
