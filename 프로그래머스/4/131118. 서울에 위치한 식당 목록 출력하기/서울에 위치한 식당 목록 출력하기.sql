-- 코드를 입력하세요
SELECT
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS,
    ROUND(AVG(R.REVIEW_SCORE), 2) as SCORE
from REST_INFO as I
    join REST_REVIEW as R
        on I.REST_ID=R.REST_ID
group by I.REST_ID
having I.ADDRESS like '서울%'
order by SCORE desc, FAVORITES desc
