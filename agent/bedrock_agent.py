
import boto3
import json
import time

class BedrockAgentClient:
    def __init__(self, region_name='us-east-1'):
        """Initialize Bedrock Agent client"""
        self.bedrock_agent = boto3.client('bedrock-agent', region_name=region_name)
        self.bedrock_agent_runtime = boto3.client('bedrock-agent-runtime', region_name=region_name)

    def create_agent(self, agent_name, instruction, agent_resource_role_arn):
        """Create a new Bedrock Agent"""
        try:
            response = self.bedrock_agent.create_agent(
                agentName=agent_name,
                instruction=instruction,
                agentResourceRoleArn=agent_resource_role_arn
            )
            return response
        except Exception as e:
            print(f"Error creating agent: {str(e)}")
            raise

    def delete_agent(self, agent_id):
        """Delete a Bedrock Agent"""
        try:
            response = self.bedrock_agent.delete_agent(
                agentId=agent_id
            )
            return response
        except Exception as e:
            print(f"Error deleting agent: {str(e)}")
            raise

    def list_agents(self):
        """List all Bedrock Agents"""
        try:
            response = self.bedrock_agent.list_agents()
            return response
        except Exception as e:
            print(f"Error listing agents: {str(e)}")
            raise

    def get_agent(self, agent_id):
        """Get details of a specific Bedrock Agent"""
        try:
            response = self.bedrock_agent.get_agent(
                agentId=agent_id
            )
            return response
        except Exception as e:
            print(f"Error getting agent details: {str(e)}")
            raise

    def invoke_agent(self, agent_id, agent_alias_id, input_text):
        """Invoke a Bedrock Agent"""
        try:
            response = self.bedrock_agent_runtime.invoke_agent(
                agentId=agent_id,
                agentAliasId=agent_alias_id,
                sessionId=str(int(time.time())),
                inputText=input_text
            )
            return response
        except Exception as e:
            print(f"Error invoking agent: {str(e)}")
            raise

    def prepare_agent(self, agent_id):
        """Prepare a Bedrock Agent"""
        try:
            response = self.bedrock_agent.prepare_agent(
                agentId=agent_id
            )
            return response
        except Exception as e:
            print(f"Error preparing agent: {str(e)}")
            raise

    def update_agent(self, agent_id, instruction=None, description=None):
        """Update a Bedrock Agent"""
        try:
            update_params = {
                'agentId': agent_id
            }
            if instruction:
                update_params['instruction'] = instruction
            if description:
                update_params['description'] = description
                
            response = self.bedrock_agent.update_agent(**update_params)
            return response
        except Exception as e:
            print(f"Error updating agent: {str(e)}")
            raise


class BedrockAgent:
    def __init__(self):
        self.client = BedrockAgentClient()

    def perform_action(self, action):
        """Perform an action using the Bedrock Agent"""
        agent_name = 'my-agent'
        instruction = action
        agent_resource_role_arn = 'arn:aws:iam::123456789012:role/bedrock-agent-role'

        # Create a new Bedrock Agent
        response = self.client.create_agent(agent_name, instruction, agent_resource_role_arn)
        agent_id = response['agentId']

        # Prepare the agent
        self.client.prepare_agent(agent_id)

        # Invoke the agent
        input_text = 'Invoke the agent'
        response = self.client.invoke_agent(agent_id, '1', input_text)
        print(json.dumps(response, indent=2))

        # Delete the agent
        self.client.delete_agent(agent_id)

    def ask_question(self, question):
        """Ask a question using the Bedrock Agent"""
        agent_name = 'my-agent'
        instruction = question
        agent_resource_role_arn = 'arn:aws:iam::123456789012:role/bedrock-agent-role'

        # Create a new Bedrock Agent
        response = self.client.create_agent(agent_name, instruction, agent_resource_role_arn)
        agent_id = response['agentId']

        # Prepare the agent
        self.client.prepare_agent(agent_id)

        # Invoke the agent
        input_text = 'Invoke the agent'
        response = self.client.invoke_agent(agent_id, '1', input_text)
        print(json.dumps(response, indent=2))

        # Delete the agent
        self.client.delete_agent(agent_id)