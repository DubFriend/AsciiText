import sublime, sublime_plugin

a = ["....###....","...##.##...","..##...##..",".##.....##.",".#########.",".##.....##.",".##.....##."]
b = [ ".########..", ".##.....##.", ".##.....##.", ".########..", ".##.....##.", ".##.....##.", ".########.."]
c = [ "..######..", ".##....##.", ".##.......", ".##.......", ".##.......", ".##....##.", "..######.."]
d = [ ".########..", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", ".########.."]
e = [ ".########.", ".##.......", ".##.......", ".######...", ".##.......", ".##.......", ".########."]
f = [ ".########.", ".##.......", ".##.......", ".######...", ".##.......", ".##.......", ".##......."]
g = [ "..######...", ".##....##..", ".##........", ".##...####.", ".##....##..", ".##....##..", "..######..."]
h = [ ".##.....##.", ".##.....##.", ".##.....##.", ".#########.", ".##.....##.", ".##.....##.", ".##.....##."]
i = [ ".####.", "..##..", "..##..", "..##..", "..##..", "..##..", ".####."]
j = [ ".......##.", ".......##.", ".......##.", ".......##.", ".##....##.", ".##....##.", "..######.."]
k = [ ".##....##.", ".##...##..", ".##..##...", ".#####....", ".##..##...", ".##...##..", ".##....##."]
l = [ ".##.......", ".##.......", ".##.......", ".##.......", ".##.......", ".##.......", ".########."]
m = [ ".##.....##.", ".###...###.", ".####.####.", ".##.###.##.", ".##.....##.", ".##.....##.", ".##.....##."]
n = [ ".##....##.", ".###...##.", ".####..##.", ".##.##.##.", ".##..####.", ".##...###.", ".##....##."]
o = [ "..#######..", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", "..#######.."]
p = [ ".########..", ".##.....##.", ".##.....##.", ".########..", ".##........", ".##........", ".##........"]
q = [ "..#######..", ".##.....##.", ".##.....##.", ".##.....##.", ".##..##.##.", ".##....##..", "..#####.##."]
r = [ ".########..", ".##.....##.", ".##.....##.", ".########..", ".##...##...", ".##....##..", ".##.....##."]
s = [ "..######..", ".##....##.", ".##.......", "..######..", ".......##.", ".##....##.", "..######.."]
t = [ ".########.", "....##....", "....##....", "....##....", "....##....", "....##....", "....##...."]
u = [ ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", "..#######.."]
v = [ ".##.....##.", ".##.....##.", ".##.....##.", ".##.....##.", "..##...##..", "...##.##...", "....###...."]
w = [ ".##......##.", ".##..##..##.", ".##..##..##.", ".##..##..##.", ".##..##..##.", ".##..##..##.", "..###..###.."]
x = [ ".##.....##.", "..##...##..", "...##.##...", "....###....", "...##.##...", "..##...##..", ".##.....##."]
y = [ ".##....##.", "..##..##..", "...####...", "....##....", "....##....", "....##....", "....##...."]
z = [ ".########.", "......##..", ".....##...", "....##....", "...##.....", "..##......", ".########."]
space = ["....","....","....","....","....","....","...."]
Alphabet = { 'A' : a, 'B' : b, 'C' : c, 'D' : d, 'E' : e, 'F' : f, 'G' : g, 'H' : h, 'I' : i, 'J' : j, \
             'K' : k, 'L' : l , 'M' : m, 'N' : n, 'O' : o, 'P' : p, 'Q' : q, 'R' : r, 'S' : s, 'T' : t, \
             'U' : u, 'V' : v, 'W' : w, 'X' : x, 'Y' : y, 'Z' : z, ' ' : space}

class AsciiTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            self.view.replace(
                edit, region, self.string_to_ascii(self.view.substr(region))
            )

    def string_to_ascii(self, in_string ):
        out_put_string = ''
        for x in range(7):
            for char in in_string.upper():
                out_put_string += Alphabet[char][x]
            out_put_string += "\n"
        return out_put_string.replace('.', ' ')
