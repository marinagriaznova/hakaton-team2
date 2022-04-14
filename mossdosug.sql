--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Чт апр 14 16:40:18 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: cinema
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
                       'Стражи терракоты',
                       'Мультфильм',
                       '12+',
                       'Молодая девушка и терракотовый воин объединяются в борьбе против монстров.',
                       'https://clck.ru/et5eT'
                   );


-- Таблица: concert
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
                        'Дайте танк (!)',
                        'Инди',
                        '16+',
                        'Adrenaline Stadium',
                        'https://clck.ru/et6js',
                        '24 апреля'
                    );


-- Таблица: pushkincard
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
                            'Шахматы',
                            '12+',
                            'Российская премьера мюзикла Тима Райса на музыку участников ABBA',
                            'https://clck.ru/etKyR'
                        );


-- Таблица: sport
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
                      'Бойцовский клуб. Суперсерия. Бой за титул РЕН ТВ',
                      '12+',
                      'https://clck.ru/et5n8',
                      29.04
                  );


-- Таблица: theatre
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
                        'Балет',
                        '12+',
                        'Гала-концерт к 45-летию Театра балета Бориса Эйфмана: сцены из лучших спектаклей и премьера',
                        'https://clck.ru/etHKd'
                    );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
