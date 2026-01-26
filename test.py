try:
    from langchain import hub
    print("Success: Imported hub from langchain")
except ImportError:
    try:
        import langchainhub as hub
        print("Success: Imported langchainhub directly")
    except ImportError:
        print("Failure: Could not find hub in any format")

# If successful, try to pull a simple prompt (requires internet)
try:
    prompt = hub.pull("rlm/rag-prompt")
    print("Hub connection verified!")
except Exception as e:
    print(f"Connection worked, but pull failed: {e}")