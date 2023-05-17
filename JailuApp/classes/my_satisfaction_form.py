from JailuApp.classes.base_structures import *
from JailuApp.models import SatisfactionForm


class TableMySatisfactionForm(TableObjectBase):
    # table specific settings
    object_name = 'my_satisfaction_form'

    # field settings
    fields = {
        "id": TableFieldBase(object_name, 'id', InputTypes.TEXT.code, ValidationTypes.NONE.code
                             , {Actions.Add.code: False, Actions.Edit.code: True, Actions.List.code: False,
                                Actions.View.code: True}
                             , {Actions.SubmitAdd.code: False, Actions.Edit.code: True,
                                Actions.SubmitEdit.code: True, Actions.Delete.code: True}
                             , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '', 'value2': ''})

        , "entry_date": TableFieldBase(object_name, 'entry_date', InputTypes.DATETIME.code, ValidationTypes.DATETIME.code
                                       , {Actions.Add.code: False, Actions.Edit.code: False, Actions.List.code: True,
                                          Actions.View.code: True}
                                       ,
                                       {Actions.Add.code: False, Actions.SubmitAdd.code: False, Actions.Edit.code: False
                                           , Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                       , {'show': True, 'filter_type': FilterTypes.BETWEEN.code, 'value': '',
                                          'value2': ''})

        , "agent": TableFieldBase(object_name, 'agent', InputTypes.DROPDOWN.code, ValidationTypes.NONE.code
                                  , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: True,
                                     Actions.View.code: True}
                                  , {Actions.Add.code: True, Actions.SubmitAdd.code: True, Actions.Edit.code: True,
                                     Actions.SubmitEdit.code: True, Actions.Delete.code: False}
                                  , {'show': True, 'filter_type': FilterTypes.LIKE.code, 'value': '', 'value2': ''})

        , "phone_number": TableFieldBase(object_name, 'phone_number', InputTypes.TEXT.code, ValidationTypes.PHONE_NUMBER_10.code
                                          , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: True,
                                             Actions.View.code: True}
                                          , {Actions.Add.code: True, Actions.SubmitAdd.code: True,
                                             Actions.Edit.code: True,
                                             Actions.SubmitEdit.code: True, Actions.Delete.code: False}
                                          , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                             'value2': ''})
        , "status": TableFieldBase(object_name, 'status', InputTypes.RADIOBUTTON.code, ValidationTypes.NONE.code
                                    , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: True,
                                       Actions.View.code: True}
                                    , {Actions.Add.code: True, Actions.SubmitAdd.code: True, Actions.Edit.code: True,
                                       Actions.SubmitEdit.code: True, Actions.Delete.code: False}
                                    , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '', 'value2': ''})


        , "consent": TableFieldBase(object_name, 'consent', InputTypes.RADIOBUTTON.code, ValidationTypes.NONE.code
                                    , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: True,
                                       Actions.View.code: True}
                                    , {Actions.Add.code: False, Actions.SubmitAdd.code: False, Actions.Edit.code: False,
                                       Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                    , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '', 'value2': ''})
        , "rate_nft_services": TableFieldBase(object_name, 'rate_nft_services', InputTypes.RADIOBUTTON.code,
                                           ValidationTypes.INT.code
                                           , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: False,
                                              Actions.View.code: True}
                                           , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                              Actions.Edit.code: False,
                                              Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                           , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                              'value2': ''})
        , "why_rate_nft_services": TableFieldBase(object_name, 'why_rate_nft_services', InputTypes.TEXTAREA.code,
                                              ValidationTypes.NONE.code
                                              , {Actions.Add.code: True, Actions.Edit.code: True,
                                                 Actions.List.code: False,
                                                 Actions.View.code: True}
                                              , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                                 Actions.Edit.code: False,
                                                 Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                              , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                                 'value2': ''})
        , "rate_nft_recommendation": TableFieldBase(object_name, 'rate_nft_recommendation', InputTypes.RADIOBUTTON.code,
                                          ValidationTypes.INT.code
                                          , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: False,
                                             Actions.View.code: True}
                                          , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                             Actions.Edit.code: False,
                                             Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                          , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                             'value2': ''})

        , "why_rate_nft_recommendation": TableFieldBase(object_name, 'why_rate_nft_recommendation', InputTypes.TEXTAREA.code,
                                                 ValidationTypes.NONE.code
                                                 , {Actions.Add.code: True, Actions.Edit.code: True,
                                                    Actions.List.code: False,
                                                    Actions.View.code: True}
                                                 , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                                    Actions.Edit.code: False,
                                                    Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                                 , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                                    'value2': ''})
        , "improve_nft_experience": TableFieldBase(object_name, 'improve_nft_experience', InputTypes.TEXTAREA.code,
                                           ValidationTypes.NONE.code
                                           , {Actions.Add.code: True, Actions.Edit.code: True, Actions.List.code: False,
                                              Actions.View.code: True}
                                           , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                              Actions.Edit.code: False,
                                              Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                           , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                              'value2': ''})

        , "any_comments": TableFieldBase(object_name, 'any_comments', InputTypes.TEXTAREA.code,
                                           ValidationTypes.NONE.code
                                           , {Actions.Add.code: True, Actions.Edit.code: True,
                                              Actions.List.code: False,
                                              Actions.View.code: True}
                                           , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                              Actions.Edit.code: False,
                                              Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                           , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                              'value2': ''})

        , "entered_by": TableFieldBase(object_name, 'entered_by', InputTypes.TEXT.code, ValidationTypes.NONE.code
                                       , {Actions.Add.code: False, Actions.Edit.code: False, Actions.List.code: False,
                                          Actions.View.code: True}
                                       , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                          Actions.Edit.code: False,
                                          Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                       ,
                                       {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '', 'value2': ''})
        , "last_modified": TableFieldBase(object_name, 'last_modified', InputTypes.TEXT.code, ValidationTypes.NONE.code
                                          ,
                                          {Actions.Add.code: False, Actions.Edit.code: False, Actions.List.code: False,
                                           Actions.View.code: True}
                                          , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                             Actions.Edit.code: False,
                                             Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                          , {'show': False, 'filter_type': FilterTypes.BETWEEN.code, 'value': '',
                                             'value2': ''})
        , "modified_by": TableFieldBase(object_name, 'modified_by', InputTypes.TEXT.code, ValidationTypes.NONE.code
                                        , {Actions.Add.code: False, Actions.Edit.code: False, Actions.List.code: False,
                                           Actions.View.code: True}
                                        , {Actions.Add.code: False, Actions.SubmitAdd.code: False,
                                           Actions.Edit.code: False,
                                           Actions.SubmitEdit.code: False, Actions.Delete.code: False}
                                        , {'show': False, 'filter_type': FilterTypes.LIKE.code, 'value': '',
                                           'value2': ''})

    }

    def select_all_records(self):
        # collect parameters
        sql_parameter = []
        # put custom implementation for model
        sql = """select det.* 
        , concat_ws(' ',ag.first_name, ag.sur_name, ag.middle_name) as agent_name
        , concat_ws(' ',eb.first_name, eb.sur_name, eb.middle_name) as entered_by_name 
        , concat_ws(' ',mb.first_name, mb.sur_name, mb.middle_name) as modified_by_name 
        from satisfaction_form det 
        left join user_account ag on ag.id = det.agent_id 
        left join user_account eb on eb.id = det.entered_by_id
        left join user_account mb on mb.id = det.modified_by_id
        where 1=1 """

        # apply filters if available
        sql += " and det.agent_id = %s "
        sql_parameter.append(current_user_id())

        # apply sort
        sql += " order by det.entry_date DESC"
        # apply limit and offset
        return dict(list=self.apply_sql_limit(sql, sql_parameter), count=self.count_sql_result(sql, sql_parameter))

        # override for lookup information
    def get_list_data(self):
            data = self.select_all_records()
            data_list = list()
            for item in data["list"]:
                an_item = dict()
                an_item["id"] = TableFieldListItem("id", item.get("id"), item.get("id"))
                an_item["agent"] = TableFieldListItem("agent", item.get("agent_id"), item.get("agent_name"))
                an_item["phone_number"] = TableFieldListItem("phone_number", item.get("phone_number"),
                                                                            item.get("phone_number"))
                an_item["status"] = TableFieldListItem("status", item.get("status"),
                                                        Lookups.get_name_by_id(item.get("status"), Lookups.yes_no_status()))
                an_item["consent"] = TableFieldListItem("consent", item.get("consent"),
                                                        Lookups.get_name_by_id(item.get("consent"), Lookups.consents()))
                an_item["rate_nft_services"] = TableFieldListItem("rate_nft_services", item.get("rate_nft_services"),
                                                               Lookups.get_name_by_id(item.get("rate_nft_services"),
                                                                                      Lookups.rate_nft_services()))
                an_item["why_rate_nft_services"] = TableFieldListItem("why_rate_nft_services", item.get("why_rate_nft_services"),
                                                                     item.get("why_rate_nft_services"))
                an_item["rate_nft_recommendation"] = TableFieldListItem("rate_nft_recommendation", item.get("rate_nft_recommendation"),
                                                              Lookups.get_name_by_id(item.get("rate_nft_recommendation"),
                                                                                     Lookups.rate_nft_recommendation()))

                an_item["why_rate_nft_recommendation"] = TableFieldListItem("why_rate_nft_recommendation",
                                                                     item.get("why_rate_nft_recommendation"),
                                                                     item.get("why_rate_nft_recommendation"))

                an_item["improve_nft_experience"] = TableFieldListItem("improve_nft_experience",
                                                                            item.get("improve_nft_experience"),
                                                                            item.get("improve_nft_experience"))

                an_item["any_comments"] = TableFieldListItem("any_comments", item.get("any_comments"),
                                                                       item.get("any_comments"))

                an_item["entry_date"] = TableFieldListItem("entry_date", item.get("entry_date"),
                                                           item.get("entry_date").strftime('%Y-%m-%d %H:%M:%S'))
                an_item["entered_by"] = TableFieldListItem("entered_by", item.get("entered_by"),
                                                           item.get("entered_by_name"))
                an_item["last_modified"] = TableFieldListItem("last_modified", item.get("last_modified"),
                                                              item.get("last_modified"))
                an_item["modified_by"] = TableFieldListItem("modified_by", item.get("modified_by"),
                                                            item.get("modified_by_name"))
                data_list.append(an_item)
            return {"list": data_list, "count": data["count"]}

    def select_a_record(self, object_id):
        # collect parameters
        sql_parameter = []
        # put custom implementation for model
        sql = """select det.* 
        , concat_ws(' ',ag.first_name, ag.sur_name, ag.middle_name) as agent_name
        , concat_ws(' ',eb.first_name, eb.sur_name, eb.middle_name) as entered_by_name 
        , concat_ws(' ',mb.first_name, mb.sur_name, mb.middle_name) as modified_by_name 
        from satisfaction_form det 
        left join user_account ag on ag.id = det.agent_id 
        left join user_account eb on eb.id = det.entered_by_id
        left join user_account mb on mb.id = det.modified_by_id
        where 1=1 """
        # apply filter
        sql += """ and det.id = %s  limit 1"""
        sql_parameter.append(str(object_id))

        return my_custom_sql(sql, sql_parameter)[0]  # get record to be edited

    def get_record_data(self, object_id):
        dict_obj = self.select_a_record(object_id)
        # if its not empty
        if dict_obj.__len__() != 0:
            for a_field in self.fields:
                if dict_obj.get(self.fields[a_field].object_name, None) is not None:
                    self.fields[a_field].current_value = dict_obj.get(self.fields[a_field].object_name)
                    self.fields[a_field].view_value = self.fields[a_field].current_value
            #  cater for foreign keys
            self.fields["agent"].current_value = dict_obj.get("agent_id")
            self.fields["agent"].view_value = dict_obj.get("agent_name")

            self.fields["status"].view_value = Lookups.get_name_by_id(dict_obj.get("status"), Lookups.yes_no_status())
            self.fields["consent"].view_value = Lookups.get_name_by_id(dict_obj.get("consent"),Lookups.consents())
            self.fields["rate_nft_services"].view_value = Lookups.get_name_by_id(dict_obj.get("rate_nft_services"), Lookups.rate_nft_services())
            self.fields["rate_nft_recommendation"].view_value = Lookups.get_name_by_id(dict_obj.get("rate_nft_recommendation"), Lookups.rate_nft_recommendation())

            self.fields["entered_by"].current_value = dict_obj.get("entered_by_id")
            self.fields["entered_by"].view_value = dict_obj.get("entered_by_name")
            self.fields["modified_by"].current_value = dict_obj.get("modified_by_id")
            self.fields["modified_by"].view_value = dict_obj.get("modified_by_name")

    def insert_row(self):
        api_response = {"error": False, "error_msg": "Insert completed successfully"}

        # clean data
        if is_empty(self.fields["consent"].current_value):
            self.fields["consent"].current_value = None
        if is_empty(self.fields["rate_nft_services"].current_value):
            self.fields["rate_nft_services"].current_value = None
        if is_empty(self.fields["why_rate_nft_services"].current_value):
            self.fields["why_rate_nft_services"].current_value = None
        if is_empty(self.fields["rate_nft_recommendation"].current_value):
            self.fields["rate_nft_recommendation"].current_value = None
        if is_empty(self.fields["why_rate_nft_recommendation"].current_value):
            self.fields["why_rate_nft_recommendation"].current_value = None
        if is_empty(self.fields["improve_nft_experience"].current_value):
            self.fields["improve_nft_experience"].current_value = None
        if is_empty(self.fields["any_comments"].current_value):
            self.fields["any_comments"].current_value = None

        # populate model and perform db operation
        SatisfactionForm(id=new_guid()
                    , agent_id=self.fields["agent"].current_value
                    , phone_number=self.fields["phone_number"].current_value
                    , status=self.fields["status"].current_value
                    , consent=self.fields["consent"].current_value
                    , rate_nft_services=self.fields["rate_nft_services"].current_value
                    , why_rate_nft_services=self.fields["why_rate_nft_services"].current_value
                    , rate_nft_recommendation=self.fields["rate_nft_recommendation"].current_value
                    , why_rate_nft_recommendation=self.fields["why_rate_nft_recommendation"].current_value
                    , improve_nft_experience=self.fields["improve_nft_experience"].current_value
                    , any_comments=self.fields["any_comments"].current_value
                    , entry_date=current_datetime()
                    , entered_by_id=current_user_id()
                    , last_modified=current_datetime()
                    , modified_by_id=current_user_id()
                    ).save()
        return api_response

    def update_row(self):
        api_response = {"error": False, "error_msg": "Insert completed successfully"}
        # populate model and perform db operation
        obj = SatisfactionForm.objects.get(id=self.fields["id"].current_value)

        # clean data
        if is_empty(self.fields["consent"].current_value):
            self.fields["consent"].current_value = None
        if is_empty(self.fields["rate_nft_services"].current_value):
            self.fields["rate_nft_services"].current_value = None
        if is_empty(self.fields["why_rate_nft_services"].current_value):
            self.fields["why_rate_nft_services"].current_value = None
        if is_empty(self.fields["rate_nft_recommendation"].current_value):
            self.fields["rate_nft_recommendation"].current_value = None
        if is_empty(self.fields["why_rate_nft_recommendation"].current_value):
            self.fields["why_rate_nft_recommendation"].current_value = None
        if is_empty(self.fields["improve_nft_experience"].current_value):
            self.fields["improve_nft_experience"].current_value = None
        if is_empty(self.fields["any_comments"].current_value):
            self.fields["any_comments"].current_value = None

        # specify updates
        #obj.agent_id = self.fields["agent"].current_value
        obj.phone_number = self.fields["phone_number"].current_value
        obj.status = self.fields["status"].current_value
        obj.consent = self.fields["consent"].current_value
        obj.rate_nft_services = self.fields["rate_nft_services"].current_value
        obj.why_rate_nft_services = self.fields["why_rate_nft_services"].current_value
        obj.rate_nft_recommendation = self.fields["rate_nft_recommendation"].current_value
        obj.why_rate_nft_recommendation = self.fields["why_rate_nft_recommendation"].current_value
        obj.improve_nft_experience = self.fields["improve_nft_experience"].current_value
        obj.any_comments = self.fields["any_comments"].current_value
        obj.last_modified = current_datetime()
        obj.modified_by_id = current_user_id()
        obj.save()
        return api_response

    def delete_row(self):
        api_response = {"error": False, "error_msg": "Delete completed successfully"}
        from django.db import IntegrityError
        try:
            # populate model and perform db operation
            obj = SatisfactionForm.objects.get(id=self.fields["id"].current_value)
            # specify updates
            obj.delete()
        except IntegrityError as e:
            api_response = {"error": True,
                            "error_msg": "Can not delete " + self.caption + " because its used elsewhere"}

        return api_response

    def html_list_form_page_load(self):
        self.fields["agent"].lookup_data = Lookups.non_developer_users()

    def html_add_form_page_load(self):
        self.fields["agent"].lookup_data = Lookups.extract_lookup('id', 'full_name', my_custom_sql("""select id, concat_ws(' ' 
        ,first_name, sur_name, middle_name) as full_name from user_account where id != 1 and id = %s """
         , [current_user_id()]))
        self.fields["agent"].default_add = current_user_id()
        self.fields["status"].lookup_data = Lookups.yes_no_status()
        self.fields["consent"].lookup_data = Lookups.consents()
        self.fields["rate_nft_services"].lookup_data = Lookups.rate_nft_services()
        self.fields["rate_nft_recommendation"].lookup_data = Lookups.rate_nft_recommendation()

    def html_edit_form_page_load(self):
        self.fields["agent"].lookup_data = Lookups.extract_lookup('id', 'full_name', my_custom_sql("""select id, concat_ws(' ' 
                ,first_name, sur_name, middle_name) as full_name from user_account where id != 1 and id = %s """
                                                                                                               ,
                                                                                                   [current_user_id()]))
        self.fields["agent"].default_add = current_user_id()
        self.fields["status"].lookup_data = Lookups.yes_no_status()
        self.fields["consent"].lookup_data = Lookups.consents()
        self.fields["rate_nft_services"].lookup_data = Lookups.rate_nft_services()
        self.fields["rate_nft_recommendation"].lookup_data = Lookups.rate_nft_recommendation()

    def html_add_form(self):
            # call page load
            self.html_add_form_page_load()

            api_response = {"header_title": self.caption + "s", "content_title": self.caption + " Add",
                            "content_body": "content_body", "content_footer": "content_footer",
                            "error": True, "error_msg": "Unknown API Error"}
            html_text = """
            <div class="card card-info">
            <div class="card-body">
            <div class='col-lg-12'>
            """
            # add all add form fields
            for a_field in self.fields:
                html_text += self.fields[a_field].html_control(self.current_action)
            html_text += """
            </div>
            </div>
            <div class="card-footer" style="display: block;">
              """ + submit_add_link(self.object_name, self.get_submit_add_return_options()) + """
              """ + self.cancel_add_link() + """
            </div>
            </div>
            """

            # add JS
            html_text += """
            <script>
            $("#x_why_rate_nft_services").attr("style","width:100%;");
            $("#x_why_rate_nft_recommendation").attr("style","width:100%;");
            $("#x_improve_nft_experience").attr("style","width:100%;");
            $("#x_any_comments").attr("style","width:100%;");
            
                function x_status_change()
                    {
                        var status = $("#x_status").val();

                        if(status == "Yes")
                        {
                        $('[control_for="x_consent"]').show();
                        }
                        else
                        {
                        $('[control_for="x_consent"]').hide();
                        }    
                    }
                    $('[data-radiofor="x_status"]').change(function(){
    				    x_status_change();
                    });

    			    //hide field initially

                    $(function () {
                        x_status_change();
                    });
            
            
            
                function x_consent_change()
                    {
                        var consent = $("#x_consent").val();

                        if(consent == "Yes")
                        {
                        $('[control_for="x_rate_nft_services"]').show();
                        $('[control_for="x_why_rate_nft_services"]').show();
                        $('[control_for="x_rate_nft_recommendation"]').show();
                        $('[control_for="x_why_rate_nft_recommendation"]').show();
                        $('[control_for="x_improve_nft_experience"]').show();
                        $('[control_for="x_any_comments"]').show();
                        }
                        else
                        {
                        $('[control_for="x_rate_nft_services"]').hide();
                        $('[control_for="x_why_rate_nft_services"]').hide();
                        $('[control_for="x_rate_nft_recommendation"]').hide();
                        $('[control_for="x_why_rate_nft_recommendation"]').hide();
                        $('[control_for="x_improve_nft_experience"]').hide();
                        $('[control_for="x_any_comments"]').hide();
                        }    
                    }
                    $('[data-radiofor="x_consent"]').change(function(){
    				    x_consent_change();
                    });

    			    //hide field initially

                    $(function () {
                        x_consent_change();
                    });

            </script>
            """

            api_response["error"] = False
            api_response["error_msg"] = "Completed Successfully"
            api_response["content_body"] = html_text
            return api_response