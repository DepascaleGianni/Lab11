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

    #troppo pesante
    @staticmethod
    def get_all_edges(a):
        conn = DBConnect.get_connection()

        result = []
        #
        cursor = conn.cursor()
        query = """ select pv.p1,pv.p2, count(distinct(*) as num 
                    from 
                    (select gds3.Product_number as ps1, gds3.`Date` as data1, gds4.Product_number as ps2, gds4.`Date` as data2 
                    from go_daily_sales gds3 , go_daily_sales gds4
                    where year(gds3.`Date`) = 2015 and year(gds4.`Date`) = 2015
                    and gds3.Product_number < gds4.Product_number
                    ) as totV,
                    (select gds1.Product_number as p1, gds2.Product_number as p2
                    from go_daily_sales gds1 , go_daily_sales gds2 
                    where gds1.Product_number != gds2.Product_number and gds2.`Date` = gds1.`Date` and gds2.Retailer_code != gds1.Retailer_code and 
                    year(gds1.`Date`) = 2015
                    ) pv
                    where (totV.ps1 = pv.p1 and totV.ps2 = pv.p2) or  (totV.ps1 =pv.p2 and totV.ps2=pv.p1)
                    group by pv.p1,pv.p2"""
        cursor.execute(query, (a,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    # troppo pesante
    @staticmethod
    def get_edge(a):
        conn = DBConnect.get_connection()
        #result = []
        cursor = conn.cursor()
        query = """select gds1.Product_number as p1, gds2.Product_number as p2
                from go_daily_sales gds1 , go_daily_sales gds2 
                where gds1.Product_number < gds2.Product_number and gds2.`Date` = gds1.`Date` and gds2.Retailer_code != gds1.Retailer_code and 
                year(gds1.`Date`) = %s"""
        cursor.execute(query, (a,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def has_edge(a,p1,p2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """ select count(gds2.`Date`) 
                    from go_daily_sales gds1 , go_daily_sales gds2 
                    where gds2.`Date` = gds1.`Date` and gds2.Retailer_code < gds1.Retailer_code and 
                    year(gds1.`Date`) = %s and ((gds1.Product_number = %s and gds2.Product_number = %s) or  (gds1.Product_number = %s and gds2.Product_number=%s))
                    """
        cursor.execute(query, (a,p1,p2,p2,p1))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_weight(a,p1,p2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """select distinct count(*)
                from
                (select gds3.Product_number as ps1, gds3.`Date` as data1, gds4.Product_number as ps2, gds4.`Date` as data2 
                from go_daily_sales gds3 , go_daily_sales gds4
                where year(gds3.`Date`) = %s and year(gds4.`Date`) = %s
                and gds3.Product_number < gds4.Product_number 
                and gds3.`Date` <= gds4.`Date` ) as totV
                where (totV.ps1 = %s and totV.ps2 = %s) or  (totV.ps1 = %s and totV.ps2=%s)
                """
        cursor.execute(query, (a,a,p1,p2,p2,p1))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_products():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
                from go_products gp 
                """
        cursor.execute(query)
        for row in cursor:
            result.append(Product(**row))
        cursor.close()
        conn.close()
        return result



