CREATE TABLE Names1(
 name_id integer,
 name_baby char(50)
 );

ALTER TABLE Names1
ADD CONSTRAINT name_pk PRIMARY KEY (name_id);

CREATE TABLE States(
state_name char(2)
);

ALTER TABLE States
ADD CONSTRAINT state_pk PRIMARY KEY (state_name);

CREATE TABLE Names_Popularity(
state_name char(2),
name_id integer,
bd_year integer,
baby_count integer
);

ALTER TABLE Names_Popularity
ADD CONSTRAINT state_fk FOREIGN KEY (state_name) REFERENCES States (state_name);

ALTER TABLE Names_Popularity
ADD CONSTRAINT name_fk FOREIGN KEY (name_id) REFERENCES Names1 (name_id);

