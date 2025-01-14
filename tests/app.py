import streamlit as st
from streamlit_blockly.streamlit import st_blockly

# Set up Dashboard
st.set_page_config(page_title="Streamlit Google Blockly Component", layout="wide", initial_sidebar_state="collapsed")

# Example toolbox XML
toolbox_xml = """
<xml xmlns="https://developers.google.com/blockly/xml">
  <category name="Logic" colour="#5C81A6">
    <block type="controls_if"></block>
    <block type="logic_compare"></block>
  </category>
</xml>
"""

# Code generator language selection
generator_language = st.selectbox("Select Code Generator Language", ["javascript", "python", "lua", "dart", "php"])

col1, col2 = st.columns([1, 3])

with col1:
    # Grid options
    with st.expander("Grid Options", expanded=False):
        st.markdown("Customize the Blockly grid settings.")
        grid_spacing = st.slider("Grid Spacing", min_value=0, max_value=100, value=30)
        grid_length = st.slider("Grid Length", min_value=0, max_value=100, value=3)
        grid_colour = st.color_picker("Grid Colour", "#ccc")
        grid_snap = st.checkbox("Snap to Grid", value=True)

    # Zoom options
    with st.expander("Zoom Options", expanded=False):
        st.markdown("Customize the Blockly zoom settings.")
        zoom_controls = st.checkbox("Show Zoom Controls", value=True)
        zoom_wheel = st.checkbox("Enable Zoom with Mouse Wheel", value=True)
        zoom_start_scale = st.slider("Initial Zoom Scale", min_value=0.1, max_value=3.0, value=1.5, step=0.1)
        zoom_max_scale = st.slider("Max Zoom Scale", min_value=0.1, max_value=5.0, value=2.0, step=0.1)
        zoom_min_scale = st.slider("Min Zoom Scale", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
        zoom_scale_speed = st.slider("Zoom Scale Speed", min_value=0.1, max_value=2.0, value=1.2, step=0.1)

    # Trashcan option
    with st.expander("Trashcan Option", expanded=False):
        st.markdown("Show or hide the Blockly trashcan.")
        trashcan = st.checkbox("Show Trashcan", value=True)

with col2:
    # Pass the updated settings to Blockly
    generated_code = st_blockly(
        generator_language=generator_language,
        width="100%",
        height="500px",
        border="1px solid #ccc",
        box_sizing="border-box",
        grid={
            "spacing": grid_spacing,
            "length": grid_length,
            "colour": grid_colour,
            "snap": grid_snap,
        },
        trashcan=trashcan,
        zoom={
            "controls": zoom_controls,
            "wheel": zoom_wheel,
            "startScale": zoom_start_scale,
            "maxScale": zoom_max_scale,
            "minScale": zoom_min_scale,
            "scaleSpeed": zoom_scale_speed,
        },
        key=f"blockly-{grid_spacing}-{grid_length}-{grid_colour}-{grid_snap}-{zoom_controls}-{zoom_wheel}-{zoom_start_scale}-{zoom_max_scale}-{zoom_min_scale}-{zoom_scale_speed}-{trashcan}",
    )

    # Display the generated code
    st.code(generated_code, language=generator_language.lower())
