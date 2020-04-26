import 'package:flutter/material.dart';
import 'package:q_less/sections/BigImage.dart';
import 'package:q_less/sections/ListState.dart';
import 'sections/TextSection.dart';

class SplashScreen extends StatelessWidget{

  @override
  Widget build(BuildContext context) {
    return Scaffold(
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
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                BigImage('assets/images/market.jpg'),
                TextSection('Welcome to the QLess App', 'We help you find the shortest lines'),
                RaisedButton(
                  child: Text('Go!'),
                  onPressed: (){
                    Navigator.of(context).push(_createRoute(context));
                  },
                )
              ],
            )
          )
        )
    );
  }
}

Route _createRoute(BuildContext context) {
  return PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) => loadNextScreen(context),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      var begin = Offset(0.0, 1.0);
      var end = Offset.zero;
      var curve = Curves.ease;

      var tween = Tween(begin: begin, end: end).chain(CurveTween(curve: curve));

      return SlideTransition(
        position: animation.drive(tween),
        child: child,
      );
    },
  );
}

Widget loadNextScreen(BuildContext context){
  MyAppState appState = MyAppState();
  appState.initState();
  return appState.build(context);
}
