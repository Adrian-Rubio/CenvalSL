import pandas as pd
from sqlalchemy import text
from database import engine

def analyze():
    query_purch = "SELECT BaseImponible FROM Vis_AEL_EvolucionCompras WHERE CodigoEmpresa = '2' AND TRY_CONVERT(date, FechaFactura) >= '2026-01-01' AND TRY_CONVERT(date, FechaFactura) <= '2026-01-31'"
    with engine.connect() as db:
        df = pd.read_sql(text(query_purch), db)
    
    total_purchases = df['BaseImponible'].sum()
    print(f'Total Purchases Jan 2026: {total_purchases:,.2f}')

if __name__ == '__main__':
    analyze()
