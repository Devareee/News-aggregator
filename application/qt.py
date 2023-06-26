from PyQt5.QtWidgets import QTableWidgetItem


def add_table_row(table, row_data):
    row = table.rowCount()
    table.setRowCount(row + 1)
    col = 0
    cell = QTableWidgetItem(str(row_data))
    table.setItem(row, col, cell)
