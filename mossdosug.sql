--
-- ���� ������������ � ������� SQLiteStudio v3.3.3 � �� ��� 14 16:40:18 2022
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: cinema
CREATE TABLE cinema (
    name        STRING,
    genre       STRING,
    age         STRING,
    discription STRING,
    link        STRING
);

INSERT INTO cinema (
                       name,
                       genre,
                       age,
                       discription,
                       link
                   )
                   VALUES (
                       '������ ���������',
                       '����������',
                       '12+',
                       '������� ������� � ������������ ���� ������������ � ������ ������ ��������.',
                       'https://clck.ru/et5eT'
                   );


-- �������: concert
CREATE TABLE concert (
    name  STRING,
    genre STRING,
    age   STRING,
    place STRING,
    link  STRING,
    date  STRING
);

INSERT INTO concert (
                        name,
                        genre,
                        age,
                        place,
                        link,
                        date
                    )
                    VALUES (
                        '����� ���� (!)',
                        '����',
                        '16+',
                        'Adrenaline Stadium',
                        'https://clck.ru/et6js',
                        '24 ������'
                    );


-- �������: pushkincard
CREATE TABLE pushkincard (
    name        STRING,
    age         STRING,
    discription STRING,
    link        STRING
);

INSERT INTO pushkincard (
                            name,
                            age,
                            discription,
                            link
                        )
                        VALUES (
                            '�������',
                            '12+',
                            '���������� �������� ������� ���� ����� �� ������ ���������� ABBA',
                            'https://clck.ru/etKyR'
                        );


-- �������: sport
CREATE TABLE sport (
    name STRING,
    age  STRING,
    link STRING,
    date STRING
);

INSERT INTO sport (
                      name,
                      age,
                      link,
                      date
                  )
                  VALUES (
                      '���������� ����. ����������. ��� �� ����� ��� ��',
                      '12+',
                      'https://clck.ru/et5n8',
                      29.04
                  );


-- �������: theatre
CREATE TABLE theatre (
    name        STRING,
    genre       STRING,
    age         STRING,
    discription STRING,
    link        STRING
);

INSERT INTO theatre (
                        name,
                        genre,
                        age,
                        discription,
                        link
                    )
                    VALUES (
                        'Eifman Gala',
                        '�����',
                        '12+',
                        '����-������� � 45-����� ������ ������ ������ �������: ����� �� ������ ���������� � ��������',
                        'https://clck.ru/etHKd'
                    );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
