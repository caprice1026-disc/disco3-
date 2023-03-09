import discord
from discord import(
    app_commands,
    ui,
    ButtonStyle,
)


from discord.app_commands import CommandTree

TOKEN = ""

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
#鯖設定するなら　guild = discord.guild(id=)

#ここで確認のUIを作成。どうにかして下の方のコードとリンクさせる必要がある。
class confomationview(discord.ui.View):
    def __init__(self, timeout=180):
        super().__init__(timeout=timeout)
        #self.send_embed = embed
        #self.send_url_view = url_view URLview使ってないから消していい
    @discord.ui.button(label="OK", style=discord.ButtonStyle.success)
    async def ok(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.channel.send(embed=self.send_embed)
    @discord.ui.button(label="NG", style=discord.ButtonStyle.gray)
    async def ng(self, button: discord.ui.Button, interaction: discord.Interaction):
        return



@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()

@tree.command(name="promotion",description="アクティブクリエイターが宣伝するためのコマンドです。")
@app_commands.describe(role="誰に送るかを指定。",text="送りたい文章を書き込んでください。")
async def promotion_command(interaction: discord.Interaction,role:discord.Role,text:str):
    #埋め込み設定
    embed = discord.Embed(title="新作の宣伝です！", description=text)
    embed.set_author(
       name=interaction.user.display_name, 
       icon_url=interaction.user.display_avatar.url, 
   ).set_footer(
       text=f"transfar from {interaction.user.display_name}",
       icon_url=interaction.user.display_avatar.url,
   )
    #ここで一回確認を取りたい　フォローアップ関数だとエラーを吐く
    #rolenameの定義の仕方(問題なし)
    rolename = role.name
    channel = client.get_channel(1042657556386033676)
    view = confomationview()
    await interaction.response.send_message(f"{rolename}へ{text}  と送信してよいですか？", ephemeral=True)
    await interaction.followup.send(view=view)

client.run(TOKEN)

#UIについてはこれを参照　https://qiita.com/Broccolingual/items/b008421e535b96c05557
#UIの組み合わせについてはこれ参照　https://qiita.com/halglobe0108/items/d6794e2104b6c90580a6#%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%81%AE%E5%9F%8B%E3%82%81%E8%BE%BC%E3%81%BF
#やること→UIをどうにかすること　他は完成している


