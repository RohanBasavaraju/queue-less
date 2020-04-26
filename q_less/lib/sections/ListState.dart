import 'package:flutter/material.dart';
import 'TextSection.dart';

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
          title: Text("QLess",
            style: TextStyle(fontSize: 36.0, color: Colors.white,
                fontWeight: FontWeight.bold),),
          centerTitle: true,
        ),
        body: Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage("assets/images/CalHacksBackground.PNG"),
              fit: BoxFit.cover,
            ),
          ),
          child: Center(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  TextSection("Proximity Settings", "Within what range would you prefer the grocery stores to be?"),
                  Text("Within: ", style: TextStyle(fontSize: 24.0, color: Colors.black,),),
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
