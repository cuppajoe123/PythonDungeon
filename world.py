import xlrd

_world = {}
starting_position = (0, 0)


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    loc = ("resources/map.xls")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for x in range(sheet.nrows):
        for y in range(sheet.ncols):
            tile_name = sheet.cell_value(x, y)
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
