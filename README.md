https://github.com/JmpM-0743/splatoon_league_corr

## How to do
```shell
$ docker build -t spl .
$ docker run --rm -it spl --name spl bash
```

## How to collect the result
```shell
$ docker cp spl:app/output .
```

## issue
あとでパッチ投げる

* `ValueError: Worksheet titles must be unicode`
  * ガチエリアとかをasciiで表現すればOK

```
root@d2ca3330ba25:/app# python main.py
Input  : ikaWidgetCSV_20201118144206.tcsv
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    class BasicTestSuite(unittest.TestCase):
  File "main.py", line 13, in BasicTestSuite
    splatoon_league_corr.calc_corr_number_of_games('ikaWidgetCSV_20201118144206.tcsv', 'output', myteam, 50)
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/splatoon_league_corr.py", line 16, in calc_corr_number_of_games
    calc_corr(filename,save_dir,myteam,0,n,0,0)
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/splatoon_league_corr.py", line 317, in calc_corr
    mkxl.outcorr(save_dir,gameslist,myteam)
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py", line 23, in outcorr
    ws_copy = wb.create_sheet(title=sheet_name)
  File "/usr/lib/python2.7/dist-packages/openpyxl/workbook/workbook.py", line 131, in create_sheet
    new_ws = Worksheet(parent=self, title=title)
  File "/usr/lib/python2.7/dist-packages/openpyxl/worksheet/worksheet.py", line 101, in __init__
    super(Worksheet, self).__init__(parent, title)
  File "/usr/lib/python2.7/dist-packages/openpyxl/workbook/child.py", line 41, in __init__
    self.title = title or self._default_title
  File "/usr/lib/python2.7/dist-packages/openpyxl/workbook/child.py", line 78, in title
    raise ValueError("Worksheet titles must be unicode")
ValueError: Worksheet titles must be unicode
```


* SyntaxError: Non-ASCII character '\xe8' in file /usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py on line 98, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
  * `# coding: utf-8`を足す

```
root@776bacdead76:/app# python main.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    import splatoon_league_corr
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/__init__.py", line 3, in <module>
    from .splatoon_league_corr import calc_corr_number_of_games
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/splatoon_league_corr.py", line 12, in <module>
    from . import mkxl
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py", line 24
SyntaxError: Non-ASCII character '\xe3' in file /usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py on line 24, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
root@776bacdead76:/app# vi /usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py
root@776bacdead76:/app# python main.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    import splatoon_league_corr
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/__init__.py", line 3, in <module>
    from .splatoon_league_corr import calc_corr_number_of_games
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/splatoon_league_corr.py", line 12, in <module>
    from . import mkxl
  File "/usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py", line 98
SyntaxError: Non-ASCII character '\xe8' in file /usr/local/lib/python2.7/dist-packages/splatoon_league_corr/mkxl.py on line 98, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

## その他
* ikaWidgetCSV_20201118144206をコミットしているけどただのログなのでヨシッ
