from mkdocs.plugins import event_priority
from mkdocs.structure.files import InclusionLevel

@event_priority(-150)
def on_files(files, config):
    # Reset inclusion for blog posts so they are recognized by blog plugin again
    for file in files:
        if "blog/posts" in file.src_path:
            file.inclusion = InclusionLevel.INCLUDED
    
    if 'material/blog' in config.plugins:
        blog_plugin = config.plugins['material/blog']
        blog_plugin.on_files(files, config=config)
        
    return files
