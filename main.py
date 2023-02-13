import discord

bot = discord.Bot() # Create a bot object

roles = []

class boog(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    for role in roles:
        @discord.ui.button(label=role.name, style=discord.ButtonStyle.primary, emoji="😎", custom_id=role.id)
        async def button_callback(self, button, interaction):
            await interaction.user.add_roles(self.role)
            print(f"Added {self.role} to {interaction.user}")
            await interaction.response.send_message(f"Added {self.role}!")
        """
        @discord.ui.button(label="Roling", style=discord.ButtonStyle.primary, emoji="😎", custom_id="bugo") # Create a button with the label "😎 Click me!" with color Blurple
        async def button_callback(self, button, interaction):
            role = interaction.guild.get_role(1072913705785892925)
            await interaction.user.add_roles(role) # Send a message when the button is clicked
            print(f"Added {role} role to {interaction.user}")
            await interaction.response.send_message(f"Added {role} role!")
        """

class MyView(discord.ui.View):
    @discord.ui.role_select(
        placeholder = "magus",
        min_values=1,
        max_values=25,
    )
    async def select_callback(self, select, interaction, ctx = None):
        ctx = await bot.get_application_context(interaction)
        roles = []
        for role in select.values:
            roles.append(role)
        await ctx.respond("This is a button!", view=boog())
#        await interaction.response.send_message(", ".join(str(role.id) for role in roles))


@bot.slash_command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

bot.run("uh oh") # Run the bot
