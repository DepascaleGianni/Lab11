from database.DB_connect import DBConnect
from model.product import Product
from model.sale import Sale


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_year():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT YEAR(Date) FROM go_daily_sales"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['YEAR(Date)'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_colors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct(Product_color) 
                from go_products gp 
                """
        cursor.execute(query)
        for row in cursor:
            result.append(row['Product_color'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodes(c):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                from go_products gp 
                where gp.Product_color = %s
                """
        cursor.execute(query, (c,))
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_edges(a):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select gds.Product_number as p,count(*) as num  
                from go_daily_sales gds, 
                (select distinct(gds1.Product_number) as p1
                from go_daily_sales gds1 , go_daily_sales gds2 
                where gds1.Product_number = gds2.Product_number and gds2.`Date` = gds1.`Date` and gds2.Retailer_code != gds1.Retailer_code and 
                year(gds1.`Date`) = 2015
                ) pv
                where gds.Product_number = pv.p1 and year(gds
                .`Date`) = 2015
                group by gds.Product_number    """
        cursor.execute(query, (a,))
        for row in cursor:
            result.append(Sale(**row))
        cursor.close()
        conn.close()
        return result


