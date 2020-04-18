use serenity::{
    model::{channel::Message, gateway::Ready, user::OnlineStatus},
    prelude::*,
};
use stopwatch::{Stopwatch};
struct Handler;

impl EventHandler for Handler {
    fn message(&self, ctx: Context, msg: Message) {
        let msgtoedit = msg.channel_id.say(&ctx.http, "Pong!?");
        let sw = Stopwatch::start_new();
        let _ = msg.channel_id.edit_message(&ctx.http, msgtoedit, |m| {
            m.content("hello")
        });
        sw.stop();
        msg.channel_id.delete_messages(&ctx.http, msgtoedit);
        let lat = sw.elapsed_ms().to_string();
        if msg.content == "!hello" {
            let msg = msg.channel_id.send_message(&ctx.http, |m| {
                m.embed(|e| {
                    e.title("Pong");
                    e.colour(0x592630);
                    e.thumbnail("https://media.discordapp.net/attachments/676846050228568090/677256001837334578/alphabet-blocks-icon.png?width=80&height=80");
                    e.description("*rust*");
                    e.field("Message Edit Latency", lat, false);
                    e.footer(|f| {
                        f.text("created by @h ឵឵#8008 <666317117154525185>");
                        f.icon_url("https://images-ext-2.discordapp.net/external/usAjIrSe-XnUxvBAv23woGW_bMvlRdMv9x6BTNCrh_Q/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/666317117154525185/da7e7f05282a984e05b625a24acea9b6.webp");
                        f
                    });
                    e
                });
                m
            });
            if let Err(why) = msg {
                println!("Error sending message: {:?}", why);
            }
        }
    }
    fn ready(&self, ctx: Context, ready: Ready) {
        ctx.set_presence(None, OnlineStatus::Idle);
        println!("{} is connected!", ready.user.name);
    }
}

fn main() {
    let mut client = Client::new("BOT-TOKEN-HERE", Handler).unwrap();

    client.start().unwrap();
}
