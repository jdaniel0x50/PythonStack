use lead_gen_business;
SELECT DATE_FORMAT(charged_datetime, "%Y-%m") AS billing_year_month, CONCAT('$', FORMAT(SUM(amount), 2)) AS total_revenue
FROM billing
WHERE DATE_FORMAT(charged_datetime, "%Y-%m") = "2012-03"
GROUP BY billing_year_month;
