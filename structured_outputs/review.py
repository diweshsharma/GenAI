from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional
import os

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

model = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

class review(TypedDict):
    key_themes : Annotated[list[str] , 'write down all the key themes that were discussed in the review']
    summary : Annotated[str ,' A brief summary of the reviwe']
    sentiment : str
    pros : Annotated[Optional[list[str]], 'write down all the pros inside the list']
  
  
structured = model.with_structured_output(review)

result = structured.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
                           """)

    
# print(result['summary'])
# print(result['sentiment'])
# print(result['key_themes'])
# print(result['pros'])

print(result)