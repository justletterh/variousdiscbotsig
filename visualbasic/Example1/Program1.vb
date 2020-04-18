Imports System.IO
Imports System.Reflection
Imports System.Threading
Imports Discord
Imports Discord.Commands
Imports Discord.WebSocket
Imports Microsoft.Extensions.Configuration
Namespace Example_1
    Module Program1
        Public _client As DiscordSocketClient
        Public _commands As CommandService

        Sub Main()
            Start().GetAwaiter().GetResult()
        End Sub
        Public Async Function Start() As Task
            Dim config = BuildConfig()
            _client = New DiscordSocketClient()
            _commands = New CommandService()
            AddEventHandlers()
            Await _commands.AddModulesAsync(Assembly.GetEntryAssembly(), Nothing)
            Await _client.LoginAsync(TokenType.Bot, config("token"))
            Await _client.StartAsync()
            Await Task.Delay(Timeout.Infinite)
        End Function
        Private Sub AddEventHandlers()
            AddHandler _client.Log, AddressOf Logger
            AddHandler _commands.Log, AddressOf Logger
            AddHandler _client.MessageReceived, AddressOf CommandHandler
            AddHandler _client.Ready, AddressOf Ready
        End Sub
        Private Async Function Ready() As Task
            Await _client.SetStatusAsync(UserStatus.Idle)
        End Function
        Private Async Function CommandHandler(ByVal message As SocketMessage) As Task
            Dim userMessage As SocketUserMessage = TryCast(message, SocketUserMessage)
            If userMessage Is Nothing OrElse userMessage.Author.IsBot Then Return
            Dim context As New SocketCommandContext(_client, userMessage)
            Dim pos As Integer = 0
            If userMessage.HasStringPrefix("", pos) OrElse userMessage.HasMentionPrefix(_client.CurrentUser, pos) Then
                Dim result As IResult = Await _commands.ExecuteAsync(context, pos, Nothing)
                If Not result.IsSuccess AndAlso Not result.Error = CommandError.UnknownCommand Then
                    Await userMessage.Channel.SendMessageAsync(result.ErrorReason)
                End If
            End If
        End Function
        Private Function Logger(ByVal message As LogMessage, Optional task As Task = Nothing) As Task
            Console.WriteLine($"{DateTime.Now,-19} [{message.Severity,8}] {message.Source}: {message.Message} {message.Exception}")
            Return Task.CompletedTask
        End Function
        Private Function BuildConfig() As IConfiguration
            Return New ConfigurationBuilder().SetBasePath(Directory.GetCurrentDirectory).AddJsonFile("config.json").Build
        End Function
    End Module
End Namespace