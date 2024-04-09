-- orders per base model 

select cbm.id, count(*) from computer_base_model cbm 
left join order_computer oc on oc.computer_base_model_id = cbm.id
group by cbm.id 

-- sum price per base model 

select cbm.id, count(*), sum(cbm.price) as "base_model_price", sum(a.price) as "addition_price" from computer_base_model cbm 
left join order_computer oc on oc.computer_base_model_id = cbm.id
left join order_computer_addition oca on oca.order_computer_id = oc.id 
left join addition a on a.id  = oca.addition_id 
group by cbm.id