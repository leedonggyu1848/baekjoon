-- 코드를 입력하세요
SELECT
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS,
    ROUND(AVG(R.REVIEW_SCORE), 2) as SCORE
from REST_INFO as I
    right join REST_REVIEW as R
        on I.REST_ID=R.REST_ID
where substr(address,1,2)='서울'
group by I.REST_ID
order by SCORE desc, FAVORITES desc