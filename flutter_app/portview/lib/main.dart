import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MaterialApp(
    home: MyApp(),
    title: 'Moinul Portfolio',
    debugShowCheckedModeBanner: false,
  ));
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: WebView(
        initialUrl: "https://moinulportfolio.herokuapp.com/",
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}
