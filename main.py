import os
import traceback

from services.AuthorizationService import AuthorizationService
from services.Tasks.BloggerTask import BloggerTask
from services.Tasks.EmbeddingTask import EmbeddingTask
from services.Tasks.FunctionTask import FunctionTask
from services.Tasks.GnomeTask import GnomeTask
from services.Tasks.HelloApiTask import HelloApiTask
from services.Tasks.InpromptTask import InpromptTask
from services.Tasks.KnowledgeTask import KnowledgeTask
from services.Tasks.LiarTask import LiarTask
from services.Tasks.Md2htmlTask import Md2htmlTask
from services.Tasks.MemeTask import MemeTask
from services.Tasks.ModerationTask import ModerationTask
from services.Tasks.OptimaldbTask import OptimaldbTask
from services.Tasks.PeopleTask import PeopleTask
from services.Tasks.RodoTask import RodoTask
from services.Tasks.SarchTask import SearchTask
from services.Tasks.ScraperTask import ScraperTask
from services.Tasks.ToolsTask import ToolsTask
from services.Tasks.WhisperTask import WhisperTask
from services.Tasks.WhoAmITask import WhoAmITask
from utils.config_manager import load_env_variables

authorization_service = AuthorizationService()

local_variables = load_env_variables()
task_to_perform = local_variables.get("TASK", "helloapi").strip()
client = local_variables.get("CLIENT", 'langchain').strip()
openai_token = os.getenv("APIKEY-OPENAI") 
aidevs_token = authorization_service.get_token(task_to_perform)

if not aidevs_token:
    print("ERROR: Lack of token from AI DEVS")
    exit(1)

try:
    def create_hello_api_instance_task() -> HelloApiTask:
        return HelloApiTask(aidevs_token)

    def create_blogger_instance_task() -> BloggerTask:
        return BloggerTask(aidevs_token, openai_token)
    
    def create_moderation_instance_task() -> ModerationTask:
        return ModerationTask(aidevs_token, openai_token)
    
    def create_liar_instance_task() -> LiarTask:
        return LiarTask(aidevs_token, openai_token)

    def create_inprompt_instance_task() -> InpromptTask:
        return InpromptTask(aidevs_token, openai_token)
    
    def create_embedding_instance_task() -> EmbeddingTask:
        return EmbeddingTask(aidevs_token, openai_token, client)
    
    def create_whisper_instance_task() -> WhisperTask:
        return WhisperTask(aidevs_token, openai_token, client)
    
    def create_function_instance_task() -> FunctionTask:
        return FunctionTask(aidevs_token, openai_token)
    
    def create_rodo_instance_task() -> RodoTask:
        return RodoTask(aidevs_token, openai_token)
    
    def create_scraper_instance_task() -> ScraperTask:
        return ScraperTask(aidevs_token, openai_token, client)
    
    def create_whoami_instance_task() -> WhoAmITask:
        return WhoAmITask(aidevs_token, openai_token, client)

    def create_search_instance_task() -> SearchTask:
        return SearchTask(aidevs_token, openai_token)
    
    def create_people_instance_task() -> PeopleTask:
        return PeopleTask(aidevs_token, openai_token, client)
    
    def create_knowledge_instance_task() -> KnowledgeTask:
        return KnowledgeTask(aidevs_token, openai_token, client)
    
    def create_tools_instance_task() -> ToolsTask:
        return ToolsTask(aidevs_token, openai_token, client)
    
    def create_gnome_instnace_task() -> GnomeTask:
        return GnomeTask(aidevs_token, openai_token, client)
    
    def create_meme_instance_task() -> MemeTask:
        return MemeTask(aidevs_token, openai_token)
    
    def create_optimaldb_instance_task() -> OptimaldbTask:
        return OptimaldbTask(aidevs_token, openai_token, client)
    
    def create_md2html_instance_task() -> Md2htmlTask:
        return Md2htmlTask(aidevs_token, openai_token)

except Exception as ex:
    print(f"ERROR: The problem occured during initalization task {task_to_perform}. Error msg: {ex}")


match task_to_perform:
    case "helloapi":
        task_instance = create_hello_api_instance_task()
    case "blogger":
        task_instance = create_blogger_instance_task()
    case "moderation":
        task_instance = create_moderation_instance_task()
    case "liar":
        task_instance = create_liar_instance_task()
    case "inprompt":
        task_instance = create_inprompt_instance_task()
    case "embedding":
        task_instance = create_embedding_instance_task()
    case "whisper":
        task_instance = create_whisper_instance_task()
    case "functions":
        task_instance = create_function_instance_task()
    case "rodo":
        task_instance = create_rodo_instance_task()
    case "scraper":
        task_instance = create_scraper_instance_task()
    case "whoami":
        task_instance = create_whoami_instance_task()
    case "search":
        task_instance = create_search_instance_task()
    case "people":
        task_instance = create_people_instance_task()
    case "knowledge":
        task_instance = create_knowledge_instance_task()
    case "tools":
        task_instance = create_tools_instance_task()
    case "gnome":
        task_instance = create_gnome_instnace_task()
    case "meme":
        task_instance = create_meme_instance_task()
    case "optimaldb":
        task_instance = create_optimaldb_instance_task()
    case "md2html":
        task_instance = create_md2html_instance_task()
    case _:
        task_instance = create_hello_api_instance_task() 

try:
    task_instance.get_task()
    task_instance.perform_task()
    task_instance.send_answer()
except Exception as ex:
    
    print(f"ERROR: The problem occured during processing task {task_to_perform}. Error msg: {ex}")
    print(traceback.print_tb(ex.__traceback__))