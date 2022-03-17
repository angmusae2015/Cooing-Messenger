from openpyxl import load_workbook


wb = load_workbook('책배송-일지.xlsx', data_only=True)


class dropdown:
    def __init__(self):
        self.menus = []     # list of menus(dropdown.menu)
        self.selectedMenu = None    # selected menu(dropdown.menu)

    def add_menus(self, title, value):  # add menus
        self.menus.append(self.menu(title, value))

    def select(self):   # ask which menu user will select
        print("Type index")
        for i in range(0, len(self.menus)):
            print(f"{i+1}. {self.menus[i].title}")

        index = int(input(">>  "))
        self.selectedMenu = self.menus[index-1]
        print(f"You've selected {self.selectedMenu.title}")

    class menu:     # menu has two attributes: title(str), value
        def __init__(self, title, value):
            self.title = title  # title is a string that will be shown to user
            self.value = value  # value is a real data of menu


class tab:
    def __init__(self):
        self.selected_sheet = None
        self.selected_date = None   # selected date(MergedCellRange)

    def select_sheet(self):     # select sheet
        dd = dropdown()
        for sheet in wb.worksheets:
            dd.add_menus(sheet.title, sheet)
        dd.select()
        self.selected_sheet = dd.selectedMenu.value

    def get_departure_date(self):   # return every merged date cell's ranges(list of MergedCellRanges)
        departureDateCells = []
        for mergedCell in self.selected_sheet.merged_cells.ranges:
            if mergedCell.start_cell.column == 1:
                departureDateCells.append(mergedCell)

        return departureDateCells

    def select_date(self):  # select merged date cell's range(MergedCellRange)
        departureDateCells = self.get_departure_date()
        dd = dropdown()
        for dateCell in departureDateCells:
            date = dateCell.start_cell
            dd.add_menus(f"{date.value.year}-{date.value.month}-{date.value.day}", dateCell)
        dd.select()
        self.selected_date = dd.selectedMenu.value

    def get_schedule(self):
        for i in range(self.selected_date.min_row, self.selected_date.max_row + 1):
            print(self.selected_sheet[f'E{i}'].value)


t = tab()
t.select_sheet()
t.select_date()
t.get_schedule()
