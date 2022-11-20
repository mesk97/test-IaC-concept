create table if not exists test_table
(
	  id bigserial primary key,
	  fld varchar(255),
	  mark varchar(255),
	  nil varchar(255)
);

insert into first_table
select data.id, case when data.id % 2 = 0 then now()::text else null end, case when data.id % 2 = 0 then 'test_string'::text else null end, null from generate_series(1, 1000) as data(id);

