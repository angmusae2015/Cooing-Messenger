from openpyxl import load_workbook


wb = load_workbook('책배송-일지.xlsx', data_only=True)


class dropdown:
    def __init__(self):
        self.menus = []
        self.selectedMenu = None

    def add_menus(self, title, value):
        self.menus.append(self.menu(title, value))

    def select(self):
        print("Type index")
        for i in range(0, len(self.menus)):
            print(f"{i+1}. {self.menus[i].title}")

        index = int(input(">>  "))
        self.selectedMenu = self.menus[index-1]
        print(f"You've selected {self.selectedMenu.title}")

    class menu:
        def __init__(self, title, value):
            self.title = title
            self.value = value


class tab:
    def __init__(self):
        self.selected_sheet = None
        self.selected_date = None

    def select_sheet(self):
        dd = dropdown()
        for sheet in wb.worksheets:
            dd.add_menus(sheet.title, sheet)
        dd.select()
        self.selected_sheet = dd.selectedMenu.value

    def get_departure_date(self):
        departureDateCells = []
        for mergedCell in self.selected_sheet.merged_cells.ranges:
            if mergedCell.start_cell.column == 1:
                departureDateCells.append(mergedCell)

        return departureDateCells

    def select_date(self):
        departureDateCells = self.get_departure_date()
        dd = dropdown()
        for dateCell in departureDateCells:
            date = dateCell.start_cell
            dd.add_menus(f"{date.value.year}-{date.value.month}-{date.value.day}", date.value.date)
        dd.select()
        self.selected_date = dd.selectedMenu.value


t = tab()
t.select_sheet()
t.select_date()
