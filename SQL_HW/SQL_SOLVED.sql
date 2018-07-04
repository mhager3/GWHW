use sakila;

# 1a
select first_name, last_name from actor;

# 1b
select concat(first_name, ' ', last_name) as `Actor Name` from actor;

#2a
select actor_id, first_name, last_name from actor where first_name = 'Joe';

# 2b
select first_name, last_name from actor where last_name like '%gen%';

# 2c
select first_name, last_name from actor where last_name like '%li%' order by last_name, first_name;

# 2d
select country_id, country from country where country in ('Afghanistan', 'Bangladesh', 'China');

# 3a
alter table actor add middle_name varchar(25) after first_name;

# 3b
alter table actor modify column middle_name blob;

# 3c 
alter table actor drop column middle_name;

# 4a 
select last_name, count(*) as Count from actor group by last_name;

# 4b 
select last_name, count(*) Count from actor group by last_name having Count > 1;

# 4c
update actor set first_name = 'HARPO' where last_name = 'Williams' and first_name = 'Groucho';
select * from actor where first_name = 'Harpo';

# 4d
update actor
set first_name = CASE
	when first_name = 'Harpo' and actor_id = 172 then first_name = 'Groucho'
    else first_name = 'Mucho Groucho'
END;
select * from actor where actor_id = 172;

# 5a. 
show create table address;

# 6a
select first_name, last_name, address from staff s join address a on (s.address_id = a.address_id);

# 6b
select first_name, last_name, sum(amount) Total_in_August
from staff s
join payment p
on (s.staff_id = p.staff_id)
WHERE payment_date >='2005-08-01 00:00:00'
AND payment_date <'2005-09-01 00:00:00'
group by first_name, last_name;

# 6c
select title `Movie`, count(actor_id) `Total actors in the movie`
from film f
join film_actor fa
on (f.film_id = fa.film_id)
group by title
order by `Total actors in the movie` desc;

# 6d. 
select title `Movie`, count(i.film_id) `Copies on hand`
from film f
join inventory i
on (f.film_id = i.film_id)
group by title
order by `Copies on hand` desc;

# 6e. 
select first_name, last_name, sum(amount) `Total paid`
from customer c
join payment p
on(c.customer_id = p.customer_id)
group by first_name, last_name
order by last_name;

# 7a. 
select title from film
where title regexp '^[K,Q]'
and language_id in
	(
		select language_id
		from language
		where name = 'English'
	);
    
# 7b. 
select first_name, last_name
from actor
where actor_id in
	(
		select actor_id
		from film_actor
		where film_id in
			(
				select film_id
				from film
				where title = 'Alone Trip'
			)
	)
order by last_name;

# 7c. 
select cu.first_name, cu.last_name, cu.email
from city as ci
inner join country as co on ci.country_id = co.country_id
inner join address as a on a.city_id = ci.city_id
inner join customer as cu on cu.address_id = a.address_id
where co.country = 'Canada';

# 7d. 
select f.title
from film_category as fc
inner join category as c on fc.category_id = c.category_id
inner join film as f on f.film_id = fc.film_id
where c.name = 'Children';

# 7e. 
select f.title movie, count(*) rent_count
from film f, inventory i, rental r
where f.film_id = i.film_id and i.inventory_id = r.inventory_id
group by movie
order by rent_count desc;

# 7f. 
select s.store_id, sum(p.amount)
from store s, payment p, inventory i, rental r
where s.store_id = i.store_id and i.inventory_id = r.inventory_id and r.rental_id = p.rental_id
group by s.store_id;

# 7g. 
select s.store_id, c.city, country.country
from store s, city c, country, address a
where s.address_id = a.address_id and a.city_id = c.city_id and c.country_id = country.country_id;

# 7h. 
select c.name category, sum(p.amount) total 
from category c, payment p, film_category fc, inventory i, rental r
where c.category_id = fc.category_id 
	and	fc.film_id = i.film_id
    and i.inventory_id = r.inventory_id
    and r.rental_id = p.rental_id
group by c.name
order by total desc
limit 5;

# 8a. 
create view `gross revenue` as
select c.name category, sum(p.amount) total 
from category c, payment p, film_category fc, inventory i, rental r
where c.category_id = fc.category_id 
	and	fc.film_id = i.film_id
    and i.inventory_id = r.inventory_id
    and r.rental_id = p.rental_id
group by c.name
order by total desc
limit 5;

# 8b. 
select * from `gross revenue`;

# 8c. 
drop view `gross revenue`;