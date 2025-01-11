import plotly.graph_objects as go

# Define your data
label = ["Bumble", "Tinder", "Hinge", "OKC", "Badoo", "POF", "Viewed Profiles",
         "Right Swipe", "Matches", ">5 messages", "Date", "Stood Up", "Ghosted",
         "Lost Interest", "No Response", "Bot", "<5 Messages", "Rejected", "Left Swipes"]

source = [0,1,2,3,4,5, 6,7,7,8,9,9,9,9,9,9,9, 7]
target = [6,6,6,6,6,6, 7,8,17,10,11,12,13,14,15,16,18,18]
value =  [9348,27899,4024,5962,342,267, 47842,43496,298,22,2,16,4,216,27,23,43198,4346]

# Define colors for nodes
node_colors = ['#66CDAA', '#FFA07A', '#98FB98', '#FF6B6B', '#DDA0DD', '#E6E6FA',
               '#87CEEB', '#87CEFA', '#FFB6C1', '#F0E68C', '#E0FFFF', '#D8BFD8',
               '#DEB887', '#FFDAB9', '#F0FFF0', '#FFF0F5', '#E6E6FA', '#FFE4E1', '#B0C4DE']

# Define colors for links
link_colors = ['#66CDAA', '#FFA07A', '#98FB98', '#FF6B6B', '#DDA0DD', '#E6E6FA',
               '#87CEEB', '#87CEFA', '#FFB6C1', '#F0E68C', '#E0FFFF', '#D8BFD8',
               '#DEB887', '#FFDAB9', '#F0FFF0', '#FFF0F5', '#E6E6FA', '#B0C4DE']

fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = label,
        color = node_colors
    ),
    link = dict(
        source = source,
        target = target,
        value = value,
        color = link_colors
    )
)])

# Update the layout
fig.update_layout(
    title_text="Dating Apps Flow",
    font_size=10,
    paper_bgcolor='white',
    plot_bgcolor='white'
)

fig.show()