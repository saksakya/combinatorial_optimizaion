## COMBINATORIAL_OPTIMIZATION

## 紹介と使い方
- 世界を変える前に、まずジーズからということで、より多くの人とマッチングできるような組合せを最適化するプロダクトを作成しました。
- 毎回の授業でよく同じ人と5回ぐらい同じ組合せになる一方、一度も一緒になったことがない人が居たりしたので何とか出来ないかと思って作成してみました。
- input用のexcel(students_list.xlsx)に生徒番号、名前(現在の入力はランダム)及び、次の授業への参加の有無、今までのグループを入力してプログラミングを実行すると、最適な組み合わせを提案してくれるexcelファイルが出力されます。

## 工夫した点
- 取り敢えずexcelで結果を取得できるようにしました。



## 苦戦した点
- 前回でpythonを結構理解したと思っていたのですが、全然わかっていませんでした。
- よく使うライブラリである、numpy, pandasを深く理解しておらず型変換に大分手こずりました。
- 一番苦労したのは、pulpの目的条件の設定です。未だにちゃんと設定できているかよくわかりません。


## 参考にした web サイトなど

- https://datadriven-rnd.com/class-organization/


## Memo

  - 使用しているライブラリ一覧取得
  - pipreqs --encoding UTF8 .
  - pip install -r requirements.txt