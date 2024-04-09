create view orders_per_base_model as 
SELECT count(*) as "count", obm.id FROM order_computer op 
inner join computer_base_model obm on obm.id = op.computer_base_model_id
group by obm.id

create view prices as
select cbm.id as "computer_base_model_id", cbm.base_price, sadd.price as "storage_price", ga.price as "gpu_price" from order_computer op 
left join order_computer_gpu_addon opg on opg.order_computer_id = op.id
left join gpu_addon ga on opg.gpu_addon_id = ga.id
left join order_computer_storage_addon ops on ops.order_computer_id = op.id 
left join storage_addon sadd on ops.storage_addon_id = sadd.id
left join computer_base_model cbm on cbm.id = op.computer_base_model_id



create view sum_per_model as
SELECT p.computer_base_model_id,  sum(p.base_price) as "sum_base_price", sum(p.storage_price) as "sum_storage_price", sum(p.gpu_price) as "sum_gpu_price",
COALESCE(sum(p.storage_price), 0) + sum(p.base_price) + COALESCE(sum(p.gpu_price), 0) as "total_sum"
FROM `prices` p 
group by p.computer_base_model_id

create view orders_by_reseller as
SELECT r.id as "reseller_id",
count(*) as "count" FROM order_computer op 
left join `order` o on o.id = op.order_id
left join reseller r on o.reseller_id = r.id 
group by r.id;


create view computer_count_per_order as 
select o.id as "order_id", count(*) as "computer_count" from order_computer op 
left join `order` o on o.id = op.order_id
group by o.id;


create view sum_per_reseller as 
select 
r.id as "reseller_id",
count(*) as "count",

sum(cbm.base_price) as "sum_base_price",
sum(sadd.price) as "sum_storage_price",
sum(ga.price) as "sum_gpu_price",
COALESCE(sum(cbm.base_price), 0) + COALESCE(sum(sadd.price), 0) + COALESCE(sum(ga.price), 0) as "total_sum"
from order_computer op 
left join order_computer_gpu_addon opg on opg.order_computer_id = op.id
left join gpu_addon ga on opg.gpu_addon_id = ga.id
left join order_computer_storage_addon ops on ops.order_computer_id = op.id 
left join storage_addon sadd on ops.storage_addon_id = sadd.id
left join computer_base_model cbm on cbm.id = op.computer_base_model_id
left join `order` o on op.order_id = o.id 
left join reseller r on o.reseller_id = r.id

group by r.id ;