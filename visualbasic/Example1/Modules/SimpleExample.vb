Imports Discord.Commands
Imports Discord.WebSocket

Namespace Example_1

    Public Class SimpleExample
        Inherits ModuleBase(Of SocketCommandContext)

        <Command("ping--")>
        <Summary("pong")>
        Public Function SayAsync() As Task
            Return ReplyAsync("im basically the same as php ***-visualbasic***")
        End Function
        <Command("stopvb--")>
        <Summary("closes bot")>
        Public Async Function closebot(Optional ByVal user As SocketGuildUser = Nothing) As Task
            Await ReplyAsync("finally, it took you long enough :tired_face:")
            Await _client.StopAsync()
        End Function
        <Command("kys--")>
        <Summary("closes all bots")>
        Public Async Function kys(Optional ByVal user As SocketGuildUser = Nothing) As Task
            Await ReplyAsync("Bye! ***-visualbasic***")
            Await _client.StopAsync()
        End Function
        <Command("whois--")>
        <Summary("Displays basic user info")>
        Public Function UserInfo(Optional ByVal user As SocketGuildUser = Nothing) As Task
            If user Is Nothing Then user = Context.User
            Return Context.Channel.SendMessageAsync($"{user.Username}#{user.Discriminator} joined **{Context.Guild.Name}** on *{user.JoinedAt.Value.ToString("f")}*")
        End Function
        <Command("chat--asshole")>
        <Summary("Displays basic user info")>
        Public Function asshole(Optional ByVal user As SocketGuildUser = Nothing) As Task
            Return Context.Channel.SendMessageAsync("thats right")
        End Function
        <Command("chat--you need help")>
        <Summary("Displays basic user info")>
        Public Function youneedhelp(Optional ByVal user As SocketGuildUser = Nothing) As Task
            Return Context.Channel.SendMessageAsync("so do you")
        End Function
        <Command("chat--bye")>
        <Summary("Displays basic user info")>
        Public Function bye(Optional ByVal user As SocketGuildUser = Nothing) As Task
            Return Context.Channel.SendMessageAsync("__**GREETINGS!!!**__")
        End Function
    End Class

End Namespace
