IceToolCntlParser.txt# Generated from IceToolCntlParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
	from .IceToolCntlParser import IceToolCntlParser
else:
	from IceToolCntlParser import IceToolCntlParser
"this is a string"
# This class defines a complete listener for a parse tree produced by IceToolCntlParser.
class IceToolCntlParserListener(ParseTreeListener):
	_eventTraceEnabled=0
	def __init__(self, event:int):
		self._eventTraceEnabled=event
	
	# Enter a parse tree produced by IceToolCntlParser#control_statements.
	def enterControl_statements(self, ctx:IceToolCntlParser.Control_statementsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterControl_statements")
		pass

	# Exit a parse tree produced by IceToolCntlParser#control_statements.
	def exitControl_statements(self, ctx:IceToolCntlParser.Control_statementsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitControl_statements")
		pass


	# Enter a parse tree produced by IceToolCntlParser#statement.
	def enterStatement(self, ctx:IceToolCntlParser.StatementContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterStatement")
		pass

	# Exit a parse tree produced by IceToolCntlParser#statement.
	def exitStatement(self, ctx:IceToolCntlParser.StatementContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitStatement")
		pass


	# Enter a parse tree produced by IceToolCntlParser#null_stmt.
	def enterNull_stmt(self, ctx:IceToolCntlParser.Null_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterNull_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#null_stmt.
	def exitNull_stmt(self, ctx:IceToolCntlParser.Null_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitNull_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comment_stmt.
	def enterComment_stmt(self, ctx:IceToolCntlParser.Comment_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComment_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comment_stmt.
	def exitComment_stmt(self, ctx:IceToolCntlParser.Comment_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComment_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#from_op.
	def enterFrom_op(self, ctx:IceToolCntlParser.From_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFrom_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#from_op.
	def exitFrom_op(self, ctx:IceToolCntlParser.From_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFrom_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#using_op.
	def enterUsing_op(self, ctx:IceToolCntlParser.Using_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterUsing_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#using_op.
	def exitUsing_op(self, ctx:IceToolCntlParser.Using_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitUsing_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#to_op.
	def enterTo_op(self, ctx:IceToolCntlParser.To_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterTo_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#to_op.
	def exitTo_op(self, ctx:IceToolCntlParser.To_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitTo_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#fnames_multi_op.
	def enterFnames_multi_op(self, ctx:IceToolCntlParser.Fnames_multi_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFnames_multi_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#fnames_multi_op.
	def exitFnames_multi_op(self, ctx:IceToolCntlParser.Fnames_multi_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFnames_multi_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#uzero_op.
	def enterUzero_op(self, ctx:IceToolCntlParser.Uzero_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterUzero_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#uzero_op.
	def exitUzero_op(self, ctx:IceToolCntlParser.Uzero_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitUzero_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#vstype_op.
	def enterVstype_op(self, ctx:IceToolCntlParser.Vstype_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterVstype_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#vstype_op.
	def exitVstype_op(self, ctx:IceToolCntlParser.Vstype_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitVstype_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#vsam_code.
	def enterVsam_code(self, ctx:IceToolCntlParser.Vsam_codeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterVsam_code")
		pass

	# Exit a parse tree produced by IceToolCntlParser#vsam_code.
	def exitVsam_code(self, ctx:IceToolCntlParser.Vsam_codeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitVsam_code")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ddname.
	def enterDdname(self, ctx:IceToolCntlParser.DdnameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDdname")
		pass

	# Exit a parse tree produced by IceToolCntlParser#ddname.
	def exitDdname(self, ctx:IceToolCntlParser.DdnameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDdname")
		pass


	# Enter a parse tree produced by IceToolCntlParser#name.
	def enterName(self, ctx:IceToolCntlParser.NameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterName")
		pass

	# Exit a parse tree produced by IceToolCntlParser#name.
	def exitName(self, ctx:IceToolCntlParser.NameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitName")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#label_name.
	def enterLabel_name(self, ctx:IceToolCntlParser.Label_nameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterLabel_name")
		pass

	# Exit a parse tree produced by IceToolCntlParser#label_name.
	def exitLabel_name(self, ctx:IceToolCntlParser.Label_nameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitLabel_name")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comma.
	def enterComma(self, ctx:IceToolCntlParser.CommaContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComma")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comma.
	def exitComma(self, ctx:IceToolCntlParser.CommaContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComma")
		pass


	# Enter a parse tree produced by IceToolCntlParser#include_stmt.
	def enterInclude_stmt(self, ctx:IceToolCntlParser.Include_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterInclude_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#include_stmt.
	def exitInclude_stmt(self, ctx:IceToolCntlParser.Include_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitInclude_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#logical_expr.
	def enterLogical_expr(self, ctx:IceToolCntlParser.Logical_exprContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterLogical_expr")
		pass

	# Exit a parse tree produced by IceToolCntlParser#logical_expr.
	def exitLogical_expr(self, ctx:IceToolCntlParser.Logical_exprContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitLogical_expr")
		pass


	# Enter a parse tree produced by IceToolCntlParser#relational_condition.
	def enterRelational_condition(self, ctx:IceToolCntlParser.Relational_conditionContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterRelational_condition")
		pass

	# Exit a parse tree produced by IceToolCntlParser#relational_condition.
	def exitRelational_condition(self, ctx:IceToolCntlParser.Relational_conditionContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitRelational_condition")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comp_field_spec.
	def enterComp_field_spec(self, ctx:IceToolCntlParser.Comp_field_specContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComp_field_spec")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comp_field_spec.
	def exitComp_field_spec(self, ctx:IceToolCntlParser.Comp_field_specContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComp_field_spec")
		pass


	# Enter a parse tree produced by IceToolCntlParser#first_byte_num.
	def enterFirst_byte_num(self, ctx:IceToolCntlParser.First_byte_numContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFirst_byte_num")
		pass

	# Exit a parse tree produced by IceToolCntlParser#first_byte_num.
	def exitFirst_byte_num(self, ctx:IceToolCntlParser.First_byte_numContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFirst_byte_num")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#comp_length.
	def enterComp_length(self, ctx:IceToolCntlParser.Comp_lengthContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComp_length")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comp_length.
	def exitComp_length(self, ctx:IceToolCntlParser.Comp_lengthContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComp_length")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comp_data_fmt.
	def enterComp_data_fmt(self, ctx:IceToolCntlParser.Comp_data_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComp_data_fmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comp_data_fmt.
	def exitComp_data_fmt(self, ctx:IceToolCntlParser.Comp_data_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComp_data_fmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comp_op.
	def enterComp_op(self, ctx:IceToolCntlParser.Comp_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComp_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comp_op.
	def exitComp_op(self, ctx:IceToolCntlParser.Comp_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComp_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comp_constant.
	def enterComp_constant(self, ctx:IceToolCntlParser.Comp_constantContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComp_constant")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comp_constant.
	def exitComp_constant(self, ctx:IceToolCntlParser.Comp_constantContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComp_constant")
		pass


	# Enter a parse tree produced by IceToolCntlParser#and_op.
	def enterAnd_op(self, ctx:IceToolCntlParser.And_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterAnd_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#and_op.
	def exitAnd_op(self, ctx:IceToolCntlParser.And_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitAnd_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#or_op.
	def enterOr_op(self, ctx:IceToolCntlParser.Or_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOr_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#or_op.
	def exitOr_op(self, ctx:IceToolCntlParser.Or_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOr_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#lines_op.
	def enterLines_op(self, ctx:IceToolCntlParser.Lines_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterLines_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#lines_op.
	def exitLines_op(self, ctx:IceToolCntlParser.Lines_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitLines_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#join_stmt.
	def enterJoin_stmt(self, ctx:IceToolCntlParser.Join_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoin_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#join_stmt.
	def exitJoin_stmt(self, ctx:IceToolCntlParser.Join_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoin_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#join_opt.
	def enterJoin_opt(self, ctx:IceToolCntlParser.Join_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoin_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#join_opt.
	def exitJoin_opt(self, ctx:IceToolCntlParser.Join_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoin_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joinkeys_stmt.
	def enterJoinkeys_stmt(self, ctx:IceToolCntlParser.Joinkeys_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoinkeys_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joinkeys_stmt.
	def exitJoinkeys_stmt(self, ctx:IceToolCntlParser.Joinkeys_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoinkeys_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_files.
	def enterJoink_files(self, ctx:IceToolCntlParser.Joink_filesContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_files")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_files.
	def exitJoink_files(self, ctx:IceToolCntlParser.Joink_filesContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_files")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_fields.
	def enterJoink_fields(self, ctx:IceToolCntlParser.Joink_fieldsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_fields")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_fields.
	def exitJoink_fields(self, ctx:IceToolCntlParser.Joink_fieldsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_fields")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_pms.
	def enterJoink_pms(self, ctx:IceToolCntlParser.Joink_pmsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_pms")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_pms.
	def exitJoink_pms(self, ctx:IceToolCntlParser.Joink_pmsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_pms")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_p.
	def enterJoink_p(self, ctx:IceToolCntlParser.Joink_pContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_p")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_p.
	def exitJoink_p(self, ctx:IceToolCntlParser.Joink_pContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_p")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#joink_m.
	def enterJoink_m(self, ctx:IceToolCntlParser.Joink_mContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_m")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_m.
	def exitJoink_m(self, ctx:IceToolCntlParser.Joink_mContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_m")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_sort_order.
	def enterJoink_sort_order(self, ctx:IceToolCntlParser.Joink_sort_orderContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_sort_order")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_sort_order.
	def exitJoink_sort_order(self, ctx:IceToolCntlParser.Joink_sort_orderContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_sort_order")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_option.
	def enterJoink_option(self, ctx:IceToolCntlParser.Joink_optionContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_option")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_option.
	def exitJoink_option(self, ctx:IceToolCntlParser.Joink_optionContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_option")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_sorted_op.
	def enterJoink_sorted_op(self, ctx:IceToolCntlParser.Joink_sorted_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_sorted_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_sorted_op.
	def exitJoink_sorted_op(self, ctx:IceToolCntlParser.Joink_sorted_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_sorted_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_type_op.
	def enterJoink_type_op(self, ctx:IceToolCntlParser.Joink_type_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_type_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_type_op.
	def exitJoink_type_op(self, ctx:IceToolCntlParser.Joink_type_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_type_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_stopaft_op.
	def enterJoink_stopaft_op(self, ctx:IceToolCntlParser.Joink_stopaft_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_stopaft_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_stopaft_op.
	def exitJoink_stopaft_op(self, ctx:IceToolCntlParser.Joink_stopaft_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_stopaft_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_taskid_op.
	def enterJoink_taskid_op(self, ctx:IceToolCntlParser.Joink_taskid_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_taskid_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_taskid_op.
	def exitJoink_taskid_op(self, ctx:IceToolCntlParser.Joink_taskid_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_taskid_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#joink_include_op.
	def enterJoink_include_op(self, ctx:IceToolCntlParser.Joink_include_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_include_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_include_op.
	def exitJoink_include_op(self, ctx:IceToolCntlParser.Joink_include_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_include_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#joink_omit_op.
	def enterJoink_omit_op(self, ctx:IceToolCntlParser.Joink_omit_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterJoink_omit_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#joink_omit_op.
	def exitJoink_omit_op(self, ctx:IceToolCntlParser.Joink_omit_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitJoink_omit_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#option_stmt.
	def enterOption_stmt(self, ctx:IceToolCntlParser.Option_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOption_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#option_stmt.
	def exitOption_stmt(self, ctx:IceToolCntlParser.Option_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOption_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#option_opt.
	def enterOption_opt(self, ctx:IceToolCntlParser.Option_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOption_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#option_opt.
	def exitOption_opt(self, ctx:IceToolCntlParser.Option_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOption_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_aresall.
	def enterOpt_aresall(self, ctx:IceToolCntlParser.Opt_aresallContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_aresall")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_aresall.
	def exitOpt_aresall(self, ctx:IceToolCntlParser.Opt_aresallContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_aresall")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_aresinv.
	def enterOpt_aresinv(self, ctx:IceToolCntlParser.Opt_aresinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_aresinv")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_aresinv.
	def exitOpt_aresinv(self, ctx:IceToolCntlParser.Opt_aresinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_aresinv")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_avgrlen.
	def enterOpt_avgrlen(self, ctx:IceToolCntlParser.Opt_avgrlenContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_avgrlen")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_avgrlen.
	def exitOpt_avgrlen(self, ctx:IceToolCntlParser.Opt_avgrlenContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_avgrlen")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_chalt.
	def enterOpt_chalt(self, ctx:IceToolCntlParser.Opt_chaltContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_chalt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_chalt.
	def exitOpt_chalt(self, ctx:IceToolCntlParser.Opt_chaltContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_chalt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_check.
	def enterOpt_check(self, ctx:IceToolCntlParser.Opt_checkContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_check")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_check.
	def exitOpt_check(self, ctx:IceToolCntlParser.Opt_checkContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_check")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_cinv.
	def enterOpt_cinv(self, ctx:IceToolCntlParser.Opt_cinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_cinv")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_cinv.
	def exitOpt_cinv(self, ctx:IceToolCntlParser.Opt_cinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_cinv")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_ckpt.
	def enterOpt_ckpt(self, ctx:IceToolCntlParser.Opt_ckptContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_ckpt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_ckpt.
	def exitOpt_ckpt(self, ctx:IceToolCntlParser.Opt_ckptContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_ckpt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_cobexit.
	def enterOpt_cobexit(self, ctx:IceToolCntlParser.Opt_cobexitContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_cobexit")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_cobexit.
	def exitOpt_cobexit(self, ctx:IceToolCntlParser.Opt_cobexitContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_cobexit")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_copy.
	def enterOpt_copy(self, ctx:IceToolCntlParser.Opt_copyContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_copy")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_copy.
	def exitOpt_copy(self, ctx:IceToolCntlParser.Opt_copyContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_copy")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_dsa.
	def enterOpt_dsa(self, ctx:IceToolCntlParser.Opt_dsaContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_dsa")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_dsa.
	def exitOpt_dsa(self, ctx:IceToolCntlParser.Opt_dsaContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_dsa")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_dspsize.
	def enterOpt_dspsize(self, ctx:IceToolCntlParser.Opt_dspsizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_dspsize")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_dspsize.
	def exitOpt_dspsize(self, ctx:IceToolCntlParser.Opt_dspsizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_dspsize")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_dynalloc.
	def enterOpt_dynalloc(self, ctx:IceToolCntlParser.Opt_dynallocContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_dynalloc")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_dynalloc.
	def exitOpt_dynalloc(self, ctx:IceToolCntlParser.Opt_dynallocContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_dynalloc")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_dynapct.
	def enterOpt_dynapct(self, ctx:IceToolCntlParser.Opt_dynapctContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_dynapct")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_dynapct.
	def exitOpt_dynapct(self, ctx:IceToolCntlParser.Opt_dynapctContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_dynapct")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_dynspc.
	def enterOpt_dynspc(self, ctx:IceToolCntlParser.Opt_dynspcContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_dynspc")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_dynspc.
	def exitOpt_dynspc(self, ctx:IceToolCntlParser.Opt_dynspcContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_dynspc")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_efs.
	def enterOpt_efs(self, ctx:IceToolCntlParser.Opt_efsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_efs")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_efs.
	def exitOpt_efs(self, ctx:IceToolCntlParser.Opt_efsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_efs")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_equals.
	def enterOpt_equals(self, ctx:IceToolCntlParser.Opt_equalsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_equals")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_equals.
	def exitOpt_equals(self, ctx:IceToolCntlParser.Opt_equalsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_equals")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_exitck.
	def enterOpt_exitck(self, ctx:IceToolCntlParser.Opt_exitckContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_exitck")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_exitck.
	def exitOpt_exitck(self, ctx:IceToolCntlParser.Opt_exitckContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_exitck")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_filsz.
	def enterOpt_filsz(self, ctx:IceToolCntlParser.Opt_filszContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_filsz")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_filsz.
	def exitOpt_filsz(self, ctx:IceToolCntlParser.Opt_filszContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_filsz")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_hiprmax.
	def enterOpt_hiprmax(self, ctx:IceToolCntlParser.Opt_hiprmaxContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_hiprmax")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_hiprmax.
	def exitOpt_hiprmax(self, ctx:IceToolCntlParser.Opt_hiprmaxContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_hiprmax")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_list.
	def enterOpt_list(self, ctx:IceToolCntlParser.Opt_listContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_list")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_list.
	def exitOpt_list(self, ctx:IceToolCntlParser.Opt_listContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_list")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_locale.
	def enterOpt_locale(self, ctx:IceToolCntlParser.Opt_localeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_locale")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_locale.
	def exitOpt_locale(self, ctx:IceToolCntlParser.Opt_localeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_locale")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_mainsize.
	def enterOpt_mainsize(self, ctx:IceToolCntlParser.Opt_mainsizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_mainsize")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_mainsize.
	def exitOpt_mainsize(self, ctx:IceToolCntlParser.Opt_mainsizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_mainsize")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_mergein.
	def enterOpt_mergein(self, ctx:IceToolCntlParser.Opt_mergeinContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_mergein")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_mergein.
	def exitOpt_mergein(self, ctx:IceToolCntlParser.Opt_mergeinContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_mergein")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_mosize.
	def enterOpt_mosize(self, ctx:IceToolCntlParser.Opt_mosizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_mosize")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_mosize.
	def exitOpt_mosize(self, ctx:IceToolCntlParser.Opt_mosizeContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_mosize")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_mowrk.
	def enterOpt_mowrk(self, ctx:IceToolCntlParser.Opt_mowrkContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_mowrk")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_mowrk.
	def exitOpt_mowrk(self, ctx:IceToolCntlParser.Opt_mowrkContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_mowrk")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_msgddn.
	def enterOpt_msgddn(self, ctx:IceToolCntlParser.Opt_msgddnContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_msgddn")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_msgddn.
	def exitOpt_msgddn(self, ctx:IceToolCntlParser.Opt_msgddnContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_msgddn")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_msgprg.
	def enterOpt_msgprg(self, ctx:IceToolCntlParser.Opt_msgprgContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_msgprg")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_msgprg.
	def exitOpt_msgprg(self, ctx:IceToolCntlParser.Opt_msgprgContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_msgprg")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_noblkset.
	def enterOpt_noblkset(self, ctx:IceToolCntlParser.Opt_noblksetContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_noblkset")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_noblkset.
	def exitOpt_noblkset(self, ctx:IceToolCntlParser.Opt_noblksetContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_noblkset")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_nooutrel.
	def enterOpt_nooutrel(self, ctx:IceToolCntlParser.Opt_nooutrelContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_nooutrel")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_nooutrel.
	def exitOpt_nooutrel(self, ctx:IceToolCntlParser.Opt_nooutrelContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_nooutrel")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_nooutsec.
	def enterOpt_nooutsec(self, ctx:IceToolCntlParser.Opt_nooutsecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_nooutsec")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_nooutsec.
	def exitOpt_nooutsec(self, ctx:IceToolCntlParser.Opt_nooutsecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_nooutsec")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_nullout.
	def enterOpt_nullout(self, ctx:IceToolCntlParser.Opt_nulloutContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_nullout")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_nullout.
	def exitOpt_nullout(self, ctx:IceToolCntlParser.Opt_nulloutContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_nullout")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_odmaxbf.
	def enterOpt_odmaxbf(self, ctx:IceToolCntlParser.Opt_odmaxbfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_odmaxbf")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_odmaxbf.
	def exitOpt_odmaxbf(self, ctx:IceToolCntlParser.Opt_odmaxbfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_odmaxbf")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_ovflo.
	def enterOpt_ovflo(self, ctx:IceToolCntlParser.Opt_ovfloContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_ovflo")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_ovflo.
	def exitOpt_ovflo(self, ctx:IceToolCntlParser.Opt_ovfloContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_ovflo")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_pad.
	def enterOpt_pad(self, ctx:IceToolCntlParser.Opt_padContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_pad")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_pad.
	def exitOpt_pad(self, ctx:IceToolCntlParser.Opt_padContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_pad")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_resall.
	def enterOpt_resall(self, ctx:IceToolCntlParser.Opt_resallContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_resall")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_resall.
	def exitOpt_resall(self, ctx:IceToolCntlParser.Opt_resallContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_resall")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_reset.
	def enterOpt_reset(self, ctx:IceToolCntlParser.Opt_resetContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_reset")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_reset.
	def exitOpt_reset(self, ctx:IceToolCntlParser.Opt_resetContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_reset")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_resinv.
	def enterOpt_resinv(self, ctx:IceToolCntlParser.Opt_resinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_resinv")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_resinv.
	def exitOpt_resinv(self, ctx:IceToolCntlParser.Opt_resinvContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_resinv")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_sdb.
	def enterOpt_sdb(self, ctx:IceToolCntlParser.Opt_sdbContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_sdb")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_sdb.
	def exitOpt_sdb(self, ctx:IceToolCntlParser.Opt_sdbContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_sdb")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_skiprec.
	def enterOpt_skiprec(self, ctx:IceToolCntlParser.Opt_skiprecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_skiprec")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_skiprec.
	def exitOpt_skiprec(self, ctx:IceToolCntlParser.Opt_skiprecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_skiprec")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_smf.
	def enterOpt_smf(self, ctx:IceToolCntlParser.Opt_smfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_smf")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_smf.
	def exitOpt_smf(self, ctx:IceToolCntlParser.Opt_smfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_smf")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_solrf.
	def enterOpt_solrf(self, ctx:IceToolCntlParser.Opt_solrfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_solrf")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_solrf.
	def exitOpt_solrf(self, ctx:IceToolCntlParser.Opt_solrfContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_solrf")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_sortdd.
	def enterOpt_sortdd(self, ctx:IceToolCntlParser.Opt_sortddContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_sortdd")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_sortdd.
	def exitOpt_sortdd(self, ctx:IceToolCntlParser.Opt_sortddContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_sortdd")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_sortin.
	def enterOpt_sortin(self, ctx:IceToolCntlParser.Opt_sortinContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_sortin")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_sortin.
	def exitOpt_sortin(self, ctx:IceToolCntlParser.Opt_sortinContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_sortin")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_spaninc.
	def enterOpt_spaninc(self, ctx:IceToolCntlParser.Opt_spanincContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_spaninc")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_spaninc.
	def exitOpt_spaninc(self, ctx:IceToolCntlParser.Opt_spanincContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_spaninc")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_stopaft.
	def enterOpt_stopaft(self, ctx:IceToolCntlParser.Opt_stopaftContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_stopaft")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_stopaft.
	def exitOpt_stopaft(self, ctx:IceToolCntlParser.Opt_stopaftContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_stopaft")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_szero.
	def enterOpt_szero(self, ctx:IceToolCntlParser.Opt_szeroContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_szero")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_szero.
	def exitOpt_szero(self, ctx:IceToolCntlParser.Opt_szeroContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_szero")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_trunc.
	def enterOpt_trunc(self, ctx:IceToolCntlParser.Opt_truncContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_trunc")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_trunc.
	def exitOpt_trunc(self, ctx:IceToolCntlParser.Opt_truncContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_trunc")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_usewkdd.
	def enterOpt_usewkdd(self, ctx:IceToolCntlParser.Opt_usewkddContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_usewkdd")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_usewkdd.
	def exitOpt_usewkdd(self, ctx:IceToolCntlParser.Opt_usewkddContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_usewkdd")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_verify.
	def enterOpt_verify(self, ctx:IceToolCntlParser.Opt_verifyContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_verify")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_verify.
	def exitOpt_verify(self, ctx:IceToolCntlParser.Opt_verifyContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_verify")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_vllong.
	def enterOpt_vllong(self, ctx:IceToolCntlParser.Opt_vllongContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_vllong")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_vllong.
	def exitOpt_vllong(self, ctx:IceToolCntlParser.Opt_vllongContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_vllong")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_vlscmp.
	def enterOpt_vlscmp(self, ctx:IceToolCntlParser.Opt_vlscmpContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_vlscmp")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_vlscmp.
	def exitOpt_vlscmp(self, ctx:IceToolCntlParser.Opt_vlscmpContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_vlscmp")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_vlshrt.
	def enterOpt_vlshrt(self, ctx:IceToolCntlParser.Opt_vlshrtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_vlshrt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_vlshrt.
	def exitOpt_vlshrt(self, ctx:IceToolCntlParser.Opt_vlshrtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_vlshrt")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#opt_vsamemt.
	def enterOpt_vsamemt(self, ctx:IceToolCntlParser.Opt_vsamemtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_vsamemt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_vsamemt.
	def exitOpt_vsamemt(self, ctx:IceToolCntlParser.Opt_vsamemtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_vsamemt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_wrkrel.
	def enterOpt_wrkrel(self, ctx:IceToolCntlParser.Opt_wrkrelContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_wrkrel")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_wrkrel.
	def exitOpt_wrkrel(self, ctx:IceToolCntlParser.Opt_wrkrelContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_wrkrel")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_wrksec.
	def enterOpt_wrksec(self, ctx:IceToolCntlParser.Opt_wrksecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_wrksec")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_wrksec.
	def exitOpt_wrksec(self, ctx:IceToolCntlParser.Opt_wrksecContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_wrksec")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_y2past.
	def enterOpt_y2past(self, ctx:IceToolCntlParser.Opt_y2pastContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_y2past")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_y2past.
	def exitOpt_y2past(self, ctx:IceToolCntlParser.Opt_y2pastContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_y2past")
		pass


	# Enter a parse tree produced by IceToolCntlParser#opt_zdprint.
	def enterOpt_zdprint(self, ctx:IceToolCntlParser.Opt_zdprintContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOpt_zdprint")
		pass

	# Exit a parse tree produced by IceToolCntlParser#opt_zdprint.
	def exitOpt_zdprint(self, ctx:IceToolCntlParser.Opt_zdprintContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOpt_zdprint")
		pass


	# Enter a parse tree produced by IceToolCntlParser#outfil_stmt.
	def enterOutfil_stmt(self, ctx:IceToolCntlParser.Outfil_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOutfil_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#outfil_stmt.
	def exitOutfil_stmt(self, ctx:IceToolCntlParser.Outfil_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOutfil_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#outfil_op.
	def enterOutfil_op(self, ctx:IceToolCntlParser.Outfil_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOutfil_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#outfil_op.
	def exitOutfil_op(self, ctx:IceToolCntlParser.Outfil_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOutfil_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#outrec_stmt.
	def enterOutrec_stmt(self, ctx:IceToolCntlParser.Outrec_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOutrec_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#outrec_stmt.
	def exitOutrec_stmt(self, ctx:IceToolCntlParser.Outrec_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOutrec_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#outrec_opt.
	def enterOutrec_opt(self, ctx:IceToolCntlParser.Outrec_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOutrec_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#outrec_opt.
	def exitOutrec_opt(self, ctx:IceToolCntlParser.Outrec_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOutrec_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#orec_fields_op.
	def enterOrec_fields_op(self, ctx:IceToolCntlParser.Orec_fields_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOrec_fields_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#orec_fields_op.
	def exitOrec_fields_op(self, ctx:IceToolCntlParser.Orec_fields_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOrec_fields_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#fld_item.
	def enterFld_item(self, ctx:IceToolCntlParser.Fld_itemContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFld_item")
		pass

	# Exit a parse tree produced by IceToolCntlParser#fld_item.
	def exitFld_item(self, ctx:IceToolCntlParser.Fld_itemContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFld_item")
		pass


	# Enter a parse tree produced by IceToolCntlParser#fnames_op.
	def enterFnames_op(self, ctx:IceToolCntlParser.Fnames_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFnames_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#fnames_op.
	def exitFnames_op(self, ctx:IceToolCntlParser.Fnames_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFnames_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#files_op.
	def enterFiles_op(self, ctx:IceToolCntlParser.Files_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFiles_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#files_op.
	def exitFiles_op(self, ctx:IceToolCntlParser.Files_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFiles_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#startrec_op.
	def enterStartrec_op(self, ctx:IceToolCntlParser.Startrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterStartrec_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#startrec_op.
	def exitStartrec_op(self, ctx:IceToolCntlParser.Startrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitStartrec_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#endrec_op.
	def enterEndrec_op(self, ctx:IceToolCntlParser.Endrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterEndrec_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#endrec_op.
	def exitEndrec_op(self, ctx:IceToolCntlParser.Endrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitEndrec_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sample_op.
	def enterSample_op(self, ctx:IceToolCntlParser.Sample_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSample_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sample_op.
	def exitSample_op(self, ctx:IceToolCntlParser.Sample_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSample_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#include_op.
	def enterInclude_op(self, ctx:IceToolCntlParser.Include_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterInclude_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#include_op.
	def exitInclude_op(self, ctx:IceToolCntlParser.Include_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitInclude_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#omit_op.
	def enterOmit_op(self, ctx:IceToolCntlParser.Omit_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOmit_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#omit_op.
	def exitOmit_op(self, ctx:IceToolCntlParser.Omit_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOmit_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#save_op.
	def enterSave_op(self, ctx:IceToolCntlParser.Save_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSave_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#save_op.
	def exitSave_op(self, ctx:IceToolCntlParser.Save_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSave_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#accept_op.
	def enterAccept_op(self, ctx:IceToolCntlParser.Accept_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterAccept_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#accept_op.
	def exitAccept_op(self, ctx:IceToolCntlParser.Accept_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitAccept_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#parse_op.
	def enterParse_op(self, ctx:IceToolCntlParser.Parse_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterParse_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#parse_op.
	def exitParse_op(self, ctx:IceToolCntlParser.Parse_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitParse_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#outrec_op.
	def enterOutrec_op(self, ctx:IceToolCntlParser.Outrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOutrec_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#outrec_op.
	def exitOutrec_op(self, ctx:IceToolCntlParser.Outrec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOutrec_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#build_op.
	def enterBuild_op(self, ctx:IceToolCntlParser.Build_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterBuild_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#build_op.
	def exitBuild_op(self, ctx:IceToolCntlParser.Build_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitBuild_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#overlay_op.
	def enterOverlay_op(self, ctx:IceToolCntlParser.Overlay_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOverlay_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#overlay_op.
	def exitOverlay_op(self, ctx:IceToolCntlParser.Overlay_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOverlay_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#findrep_op.
	def enterFindrep_op(self, ctx:IceToolCntlParser.Findrep_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFindrep_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#findrep_op.
	def exitFindrep_op(self, ctx:IceToolCntlParser.Findrep_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFindrep_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ifthen_op.
	def enterIfthen_op(self, ctx:IceToolCntlParser.Ifthen_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterIfthen_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#ifthen_op.
	def exitIfthen_op(self, ctx:IceToolCntlParser.Ifthen_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitIfthen_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ftov_op.
	def enterFtov_op(self, ctx:IceToolCntlParser.Ftov_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFtov_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#ftov_op.
	def exitFtov_op(self, ctx:IceToolCntlParser.Ftov_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFtov_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#vltrim_op.
	def enterVltrim_op(self, ctx:IceToolCntlParser.Vltrim_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterVltrim_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#vltrim_op.
	def exitVltrim_op(self, ctx:IceToolCntlParser.Vltrim_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitVltrim_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#vltrail_op.
	def enterVltrail_op(self, ctx:IceToolCntlParser.Vltrail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterVltrail_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#vltrail_op.
	def exitVltrail_op(self, ctx:IceToolCntlParser.Vltrail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitVltrail_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#repeat_op.
	def enterRepeat_op(self, ctx:IceToolCntlParser.Repeat_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterRepeat_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#repeat_op.
	def exitRepeat_op(self, ctx:IceToolCntlParser.Repeat_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitRepeat_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#split_op.
	def enterSplit_op(self, ctx:IceToolCntlParser.Split_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSplit_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#split_op.
	def exitSplit_op(self, ctx:IceToolCntlParser.Split_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSplit_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#nullofl_op.
	def enterNullofl_op(self, ctx:IceToolCntlParser.Nullofl_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterNullofl_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#nullofl_op.
	def exitNullofl_op(self, ctx:IceToolCntlParser.Nullofl_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitNullofl_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#header1_op.
	def enterHeader1_op(self, ctx:IceToolCntlParser.Header1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterHeader1_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#header1_op.
	def exitHeader1_op(self, ctx:IceToolCntlParser.Header1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitHeader1_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#trailer1_op.
	def enterTrailer1_op(self, ctx:IceToolCntlParser.Trailer1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterTrailer1_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#trailer1_op.
	def exitTrailer1_op(self, ctx:IceToolCntlParser.Trailer1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitTrailer1_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#header2_op.
	def enterHeader2_op(self, ctx:IceToolCntlParser.Header2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterHeader2_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#header2_op.
	def exitHeader2_op(self, ctx:IceToolCntlParser.Header2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitHeader2_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#trailer2_op.
	def enterTrailer2_op(self, ctx:IceToolCntlParser.Trailer2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterTrailer2_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#trailer2_op.
	def exitTrailer2_op(self, ctx:IceToolCntlParser.Trailer2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitTrailer2_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sections_op.
	def enterSections_op(self, ctx:IceToolCntlParser.Sections_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSections_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sections_op.
	def exitSections_op(self, ctx:IceToolCntlParser.Sections_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSections_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#nodetail_op.
	def enterNodetail_op(self, ctx:IceToolCntlParser.Nodetail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterNodetail_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#nodetail_op.
	def exitNodetail_op(self, ctx:IceToolCntlParser.Nodetail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitNodetail_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#blkcch1_op.
	def enterBlkcch1_op(self, ctx:IceToolCntlParser.Blkcch1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterBlkcch1_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#blkcch1_op.
	def exitBlkcch1_op(self, ctx:IceToolCntlParser.Blkcch1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitBlkcch1_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#blkcch2_op.
	def enterBlkcch2_op(self, ctx:IceToolCntlParser.Blkcch2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterBlkcch2_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#blkcch2_op.
	def exitBlkcch2_op(self, ctx:IceToolCntlParser.Blkcch2_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitBlkcch2_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#blkcct1_op.
	def enterBlkcct1_op(self, ctx:IceToolCntlParser.Blkcct1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterBlkcct1_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#blkcct1_op.
	def exitBlkcct1_op(self, ctx:IceToolCntlParser.Blkcct1_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitBlkcct1_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#removecc_op.
	def enterRemovecc_op(self, ctx:IceToolCntlParser.Removecc_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterRemovecc_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#removecc_op.
	def exitRemovecc_op(self, ctx:IceToolCntlParser.Removecc_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitRemovecc_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#iftrail_op.
	def enterIftrail_op(self, ctx:IceToolCntlParser.Iftrail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterIftrail_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#iftrail_op.
	def exitIftrail_op(self, ctx:IceToolCntlParser.Iftrail_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitIftrail_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#test_stmt.
	def enterTest_stmt(self, ctx:IceToolCntlParser.Test_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterTest_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#test_stmt.
	def exitTest_stmt(self, ctx:IceToolCntlParser.Test_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitTest_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#blob_op.
	def enterBlob_op(self, ctx:IceToolCntlParser.Blob_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterBlob_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#blob_op.
	def exitBlob_op(self, ctx:IceToolCntlParser.Blob_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitBlob_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ddname_token.
	def enterDdname_token(self, ctx:IceToolCntlParser.Ddname_tokenContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDdname_token")
		pass

	# Exit a parse tree produced by IceToolCntlParser#ddname_token.
	def exitDdname_token(self, ctx:IceToolCntlParser.Ddname_tokenContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDdname_token")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ddname_tokens.
	def enterDdname_tokens(self, ctx:IceToolCntlParser.Ddname_tokensContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDdname_tokens")
		pass

	# Exit a parse tree produced by IceToolCntlParser#ddname_tokens.
	def exitDdname_tokens(self, ctx:IceToolCntlParser.Ddname_tokensContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDdname_tokens")
		pass


	# Enter a parse tree produced by IceToolCntlParser#reformat_stmt.
	def enterReformat_stmt(self, ctx:IceToolCntlParser.Reformat_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterReformat_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#reformat_stmt.
	def exitReformat_stmt(self, ctx:IceToolCntlParser.Reformat_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitReformat_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#refor_field_op.
	def enterRefor_field_op(self, ctx:IceToolCntlParser.Refor_field_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterRefor_field_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#refor_field_op.
	def exitRefor_field_op(self, ctx:IceToolCntlParser.Refor_field_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitRefor_field_op")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#refor_fill_opt.
	def enterRefor_fill_opt(self, ctx:IceToolCntlParser.Refor_fill_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterRefor_fill_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#refor_fill_opt.
	def exitRefor_fill_opt(self, ctx:IceToolCntlParser.Refor_fill_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitRefor_fill_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#start_leng_pair.
	def enterStart_leng_pair(self, ctx:IceToolCntlParser.Start_leng_pairContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterStart_leng_pair")
		pass

	# Exit a parse tree produced by IceToolCntlParser#start_leng_pair.
	def exitStart_leng_pair(self, ctx:IceToolCntlParser.Start_leng_pairContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitStart_leng_pair")
		pass


	# Enter a parse tree produced by IceToolCntlParser#select_stmt.
	def enterSelect_stmt(self, ctx:IceToolCntlParser.Select_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#select_stmt.
	def exitSelect_stmt(self, ctx:IceToolCntlParser.Select_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#discard_op.
	def enterDiscard_op(self, ctx:IceToolCntlParser.Discard_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDiscard_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#discard_op.
	def exitDiscard_op(self, ctx:IceToolCntlParser.Discard_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDiscard_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#on_op.
	def enterOn_op(self, ctx:IceToolCntlParser.On_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterOn_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#on_op.
	def exitOn_op(self, ctx:IceToolCntlParser.On_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitOn_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#select_opt.
	def enterSelect_opt(self, ctx:IceToolCntlParser.Select_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#select_opt.
	def exitSelect_opt(self, ctx:IceToolCntlParser.Select_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#select_fmt.
	def enterSelect_fmt(self, ctx:IceToolCntlParser.Select_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_fmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#select_fmt.
	def exitSelect_fmt(self, ctx:IceToolCntlParser.Select_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_fmt")
		pass
		
	# Enter a parse tree produced by IceToolCntlParser#sort_stmt.
	def enterSort_stmt(self, ctx:IceToolCntlParser.Sort_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_stmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_stmt.
	def exitSort_stmt(self, ctx:IceToolCntlParser.Sort_stmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_stmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_opt.
	def enterSort_opt(self, ctx:IceToolCntlParser.Sort_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_opt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_opt.
	def exitSort_opt(self, ctx:IceToolCntlParser.Sort_optContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_opt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_fields_op.
	def enterSort_fields_op(self, ctx:IceToolCntlParser.Sort_fields_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_fields_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_fields_op.
	def exitSort_fields_op(self, ctx:IceToolCntlParser.Sort_fields_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_fields_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_fields_spec.
	def enterSort_fields_spec(self, ctx:IceToolCntlParser.Sort_fields_specContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_fields_spec")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_fields_spec.
	def exitSort_fields_spec(self, ctx:IceToolCntlParser.Sort_fields_specContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_fields_spec")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_pmfs.
	def enterSort_pmfs(self, ctx:IceToolCntlParser.Sort_pmfsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_pmfs")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_pmfs.
	def exitSort_pmfs(self, ctx:IceToolCntlParser.Sort_pmfsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_pmfs")
		pass


	# Enter a parse tree produced by IceToolCntlParser#format_op.
	def enterFormat_op(self, ctx:IceToolCntlParser.Format_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFormat_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#format_op.
	def exitFormat_op(self, ctx:IceToolCntlParser.Format_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFormat_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#ckpt_op.
	def enterCkpt_op(self, ctx:IceToolCntlParser.Ckpt_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterCkpt_op")
		pass
		
	# Exit a parse tree produced by IceToolCntlParser#ckpt_op.
	def exitCkpt_op(self, ctx:IceToolCntlParser.Ckpt_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitCkpt_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#dynalloc_op.
	def enterDynalloc_op(self, ctx:IceToolCntlParser.Dynalloc_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDynalloc_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#dynalloc_op.
	def exitDynalloc_op(self, ctx:IceToolCntlParser.Dynalloc_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDynalloc_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#equals_op.
	def enterEquals_op(self, ctx:IceToolCntlParser.Equals_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterEquals_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#equals_op.
	def exitEquals_op(self, ctx:IceToolCntlParser.Equals_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitEquals_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#filsz_op.
	def enterFilsz_op(self, ctx:IceToolCntlParser.Filsz_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFilsz_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#filsz_op.
	def exitFilsz_op(self, ctx:IceToolCntlParser.Filsz_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFilsz_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#skiprec_op.
	def enterSkiprec_op(self, ctx:IceToolCntlParser.Skiprec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSkiprec_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#skiprec_op.
	def exitSkiprec_op(self, ctx:IceToolCntlParser.Skiprec_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSkiprec_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#stopaft_op.
	def enterStopaft_op(self, ctx:IceToolCntlParser.Stopaft_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterStopaft_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#stopaft_op.
	def exitStopaft_op(self, ctx:IceToolCntlParser.Stopaft_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitStopaft_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#y2past_op.
	def enterY2past_op(self, ctx:IceToolCntlParser.Y2past_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterY2past_op")
		pass

	# Exit a parse tree produced by IceToolCntlParser#y2past_op.
	def exitY2past_op(self, ctx:IceToolCntlParser.Y2past_opContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitY2past_op")
		pass


	# Enter a parse tree produced by IceToolCntlParser#start_pos.
	def enterStart_pos(self, ctx:IceToolCntlParser.Start_posContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterStart_pos")
		pass
		
	# Exit a parse tree produced by IceToolCntlParser#start_pos.
	def exitStart_pos(self, ctx:IceToolCntlParser.Start_posContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitStart_pos")
		pass


	# Enter a parse tree produced by IceToolCntlParser#length.
	def enterLength(self, ctx:IceToolCntlParser.LengthContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterLength")
		pass

	# Exit a parse tree produced by IceToolCntlParser#length.
	def exitLength(self, ctx:IceToolCntlParser.LengthContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitLength")
		pass


	# Enter a parse tree produced by IceToolCntlParser#dev_name.
	def enterDev_name(self, ctx:IceToolCntlParser.Dev_nameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterDev_name")
		pass

	# Exit a parse tree produced by IceToolCntlParser#dev_name.
	def exitDev_name(self, ctx:IceToolCntlParser.Dev_nameContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitDev_name")
		pass


	# Enter a parse tree produced by IceToolCntlParser#max_work_ds.
	def enterMax_work_ds(self, ctx:IceToolCntlParser.Max_work_dsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterMax_work_ds")
		pass

	# Exit a parse tree produced by IceToolCntlParser#max_work_ds.
	def exitMax_work_ds(self, ctx:IceToolCntlParser.Max_work_dsContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitMax_work_ds")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_fields_fmt.
	def enterSort_fields_fmt(self, ctx:IceToolCntlParser.Sort_fields_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_fields_fmt")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_fields_fmt.
	def exitSort_fields_fmt(self, ctx:IceToolCntlParser.Sort_fields_fmtContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_fields_fmt")
		pass


	# Enter a parse tree produced by IceToolCntlParser#sort_fields_order.
	def enterSort_fields_order(self, ctx:IceToolCntlParser.Sort_fields_orderContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_fields_order")
		pass

	# Exit a parse tree produced by IceToolCntlParser#sort_fields_order.
	def exitSort_fields_order(self, ctx:IceToolCntlParser.Sort_fields_orderContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_fields_order")
		pass


	# Enter a parse tree produced by IceToolCntlParser#integer.
	def enterInteger(self, ctx:IceToolCntlParser.IntegerContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterInteger")
		pass

	# Exit a parse tree produced by IceToolCntlParser#integer.
	def exitInteger(self, ctx:IceToolCntlParser.IntegerContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitInteger")
		pass


	# Enter a parse tree produced by IceToolCntlParser#floatnum.
	def enterFloatnum(self, ctx:IceToolCntlParser.FloatnumContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterFloatnum")
		pass
		
	# Exit a parse tree produced by IceToolCntlParser#floatnum.
	def exitFloatnum(self, ctx:IceToolCntlParser.FloatnumContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitFloatnum")
		pass


	# Enter a parse tree produced by IceToolCntlParser#string.
	def enterString(self, ctx:IceToolCntlParser.StringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterString")
		pass

	# Exit a parse tree produced by IceToolCntlParser#string.
	def exitString(self, ctx:IceToolCntlParser.StringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitString")
		pass


	# Enter a parse tree produced by IceToolCntlParser#qstring.
	def enterQstring(self, ctx:IceToolCntlParser.QstringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterQstring")
		pass

	# Exit a parse tree produced by IceToolCntlParser#qstring.
	def exitQstring(self, ctx:IceToolCntlParser.QstringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitQstring")
		pass


	# Enter a parse tree produced by IceToolCntlParser#hexstring.
	def enterHexstring(self, ctx:IceToolCntlParser.HexstringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterHexstring")
		pass

	# Exit a parse tree produced by IceToolCntlParser#hexstring.
	def exitHexstring(self, ctx:IceToolCntlParser.HexstringContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitHexstring")
		pass


	# Enter a parse tree produced by IceToolCntlParser#char_str_constant.
	def enterChar_str_constant(self, ctx:IceToolCntlParser.Char_str_constantContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterChar_str_constant")
		pass

	# Exit a parse tree produced by IceToolCntlParser#char_str_constant.
	def exitChar_str_constant(self, ctx:IceToolCntlParser.Char_str_constantContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitChar_str_constant")
		pass


	# Enter a parse tree produced by IceToolCntlParser#question_mark.
	def enterQuestion_mark(self, ctx:IceToolCntlParser.Question_markContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterQuestion_mark")
		pass

	# Exit a parse tree produced by IceToolCntlParser#question_mark.
	def exitQuestion_mark(self, ctx:IceToolCntlParser.Question_markContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitQuestion_mark")
		pass


	# Enter a parse tree produced by IceToolCntlParser#comment_phrase.
	def enterComment_phrase(self, ctx:IceToolCntlParser.Comment_phraseContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterComment_phrase")
		pass

	# Exit a parse tree produced by IceToolCntlParser#comment_phrase.
	def exitComment_phrase(self, ctx:IceToolCntlParser.Comment_phraseContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitComment_phrase")
		pass


	# Enter a parse tree produced by IceToolCntlParser#eol.
	def enterEol(self, ctx:IceToolCntlParser.EolContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... enterEol")
		pass
		
	# Exit a parse tree produced by IceToolCntlParser#eol.
	def exitEol(self, ctx:IceToolCntlParser.EolContext):
		if self._eventTraceEnabled is 1:
			self._log.write("listener ... exitEol")
		pass
