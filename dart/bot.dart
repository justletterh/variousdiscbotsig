import 'package:nyxx/nyxx.dart';
import 'package:nyxx/Vm.dart';
import 'dart:io';
void main() {
  final bot = NyxxVm("BOT-TOKEN-HERE");
  bot.onReady.listen((e) {
    bot.self.setPresence(status: "idle", afk: false, game: Presence.of(""));
    print("Ready!");
  });
  bot.onMessageReceived.listen((MessageEvent e) {
    if (e.message.content == "ping--") {
      e.message.channel.send(content: "this bot is litrally just for ascii-text porn ***-dart***");
    }
    if (e.message.content == "stopdart--") {
      e.message.channel.send(content: ":tired_face: ***-dart***");
      bot.close();
      Future.delayed(const Duration(seconds: 3), () {
        exit(0);
      });
    }
  });
}
