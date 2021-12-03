--3aTruy suất tổng hoa hồng (commission) cho mỗi thành phố (city) 
SELECT SUM(commission)
FROM salesman 
BY city;
--3b-Truy suất tất cả khách hàng(customer)mà có người môi giới (sales_man) tương ứng có hoa hồng >0,12, sắp xếp theo hoa hồng (commission)
select * from customer 
join salesman s on c.salesman_id = s.salesman_id 
where s.commission > 0.12 
order by s.commission