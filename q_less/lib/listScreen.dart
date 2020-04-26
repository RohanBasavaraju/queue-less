import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    return MyAppState();
  }
}

class MyAppState extends State<MyApp> {
  List _distances = ["1 Mile", "5 Miles", "10 Miles", "20 Miles", "50+ Miles"];

  List<DropdownMenuItem<String>> _dropDownMenuItems;
  String _selectedDistance;

  @override
  void initState() {
    _dropDownMenuItems = buildAndGetDropDownMenuItems(_distances);
    _selectedDistance = _dropDownMenuItems[0].value;
    super.initState();
  }

  List<DropdownMenuItem<String>> buildAndGetDropDownMenuItems(List distances) {
    List<DropdownMenuItem<String>> items = List();
    for (String distance in distances) {
      items.add(DropdownMenuItem(value: distance, child: Text(distance)));
    }
    return items;
  }

  void changedDropDownItem(String selectedDistance) {
    setState(() {
      _selectedDistance = selectedDistance;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          title: Text("How Close Would You Prefer Your Store to be?",
            style: TextStyle(fontSize: 36.0, color: Colors.white,
                fontWeight: FontWeight.bold),),
          centerTitle: true,
        ),
        body: Container(
          child: Center(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text("Within: "),
                  DropdownButton(
                    value: _selectedDistance,
                    items: _dropDownMenuItems,
                    onChanged: changedDropDownItem,
                  )
                ],
              )),
        ),
      ),
    );
  }
}
