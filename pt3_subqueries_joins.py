# Part 3: Subqueries & Joins


def top_postcodes_for_chain_stores():
    """
    From the businesses table, select the top 10 most popular postal_code.
    They should be filtered to only count the restaurants owned by people/entities that own 5 or more restaurants.
    The result should:
    * return a row (postal_code, frequency) for each 10 selection
    * sort by descending order to get the most relevant zip codes
    :return: a string representing the SQL query
    :rtype: str
    """

    sql_query = """\SELECT postal_code, COUNT(*) AS frequency
    FROM businesses
    WHERE owner_name IN (
    SELECT DISTINCT(owner_name)
    FROM (SELECT owner_name, COUNT(business_id) AS num_restaurants
    FROM businesses
    GROUP BY owner_name
    ORDER BY num_restaurants DESC) AS restaurant_owners
    WHERE restaurant_owners.num_restaurants >= 5)
    GROUP BY postal_code
    ORDER BY frequency DESC
    LIMIT 10"""

    return sql_query



def inspection_scores_in_94103():
    """
    First let's get an idea about the inspection score our competition has.
    Based on multiple inspections, find out the minimum Score (as "min_score"),
    average Score (as "avg_score") and maximum Score (as "max_score") for all restaurant in post code "94103".
    The average score should be rounded to one decimal.
    :return: a string representing the SQL query
    :rtype: str
    """

    sql_query = """\
    SELECT
    MIN(ins.Score) as min_score, 
    ROUND(AVG(ins.Score), 1) as avg_score,
    MAX(ins.Score) as max_score
    FROM businesses as res
    INNER JOIN inspections as ins
    ON res.business_id == ins.business_id
    WHERE ins.Score NOT NULL
    AND res.postal_code == '94103'"""
    return sql_query




def risk_categories_in_94103():
    """
    Now lets get more serious, and look at how many times restaurants with postal code 94103
    (that's Market street) has committed health violations and group them based on their risk category.
    The output should be (risk_category, count as frequency) and sorted in descending order by frequency
    :return: a string representing the SQL query
    :rtype: str
    """

    raise NotImplementedError


