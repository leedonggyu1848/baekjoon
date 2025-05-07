# -- 코드를 작성해주세요
select c2.id as ID
from  (select * from ECOLI_DATA where parent_id is null) as c0
inner join ECOLI_DATA as c1
    on c0.id=c1.parent_id
inner join ECOLI_DATA as c2
    on c1.id=c2.parent_id
where not c2.parent_id=c2.id
order by c2.id