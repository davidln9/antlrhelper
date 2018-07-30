# Generated from IceToolToolinParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and . in __name__:
	from .IceToolToolinParser import IceToolToolinParser
else:
	from IceToolToolinParser import IceToolToolinParser

# This class defines a complete listener for a parse tree produced by IceToolToolinParser.
class IceToolToolinParserListener(ParseTreeListener):

	# Enter a parse tree produced by IceToolToolinParser#toolin_statements.
	def enterToolin_statements(self, ctx:IceToolToolinParser.Toolin_statementsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterToolin_statements")
		pass

	# Exit a parse tree produced by IceToolToolinParser#toolin_statements.
	def exitToolin_statements(self, ctx:IceToolToolinParser.Toolin_statementsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitToolin_statements")
		pass


	# Enter a parse tree produced by IceToolToolinParser#operator_statement.
	def enterOperator_statement(self, ctx:IceToolToolinParser.Operator_statementContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOperator_statement")
		pass

	# Exit a parse tree produced by IceToolToolinParser#operator_statement.
	def exitOperator_statement(self, ctx:IceToolToolinParser.Operator_statementContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOperator_statement")
		pass


	# Enter a parse tree produced by IceToolToolinParser#null_stmt.
	def enterNull_stmt(self, ctx:IceToolToolinParser.Null_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterNull_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#null_stmt.
	def exitNull_stmt(self, ctx:IceToolToolinParser.Null_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitNull_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#comment_stmt.
	def enterComment_stmt(self, ctx:IceToolToolinParser.Comment_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterComment_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#comment_stmt.
	def exitComment_stmt(self, ctx:IceToolToolinParser.Comment_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitComment_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#copy_stmt.
	def enterCopy_stmt(self, ctx:IceToolToolinParser.Copy_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCopy_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#copy_stmt.
	def exitCopy_stmt(self, ctx:IceToolToolinParser.Copy_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCopy_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#copy_ops.
	def enterCopy_ops(self, ctx:IceToolToolinParser.Copy_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCopy_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#copy_ops.
	def exitCopy_ops(self, ctx:IceToolToolinParser.Copy_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCopy_ops")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#count_stmt.
	def enterCount_stmt(self, ctx:IceToolToolinParser.Count_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCount_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#count_stmt.
	def exitCount_stmt(self, ctx:IceToolToolinParser.Count_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCount_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#count_ops.
	def enterCount_ops(self, ctx:IceToolToolinParser.Count_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCount_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#count_ops.
	def exitCount_ops(self, ctx:IceToolToolinParser.Count_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCount_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#count_opt.
	def enterCount_opt(self, ctx:IceToolToolinParser.Count_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCount_opt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#count_opt.
	def exitCount_opt(self, ctx:IceToolToolinParser.Count_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCount_opt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#datasort_stmt.
	def enterDatasort_stmt(self, ctx:IceToolToolinParser.Datasort_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDatasort_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#datasort_stmt.
	def exitDatasort_stmt(self, ctx:IceToolToolinParser.Datasort_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDatasort_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#datasort_ops.
	def enterDatasort_ops(self, ctx:IceToolToolinParser.Datasort_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDatasort_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#datasort_ops.
	def exitDatasort_ops(self, ctx:IceToolToolinParser.Datasort_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDatasort_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#defaults_stmt.
	def enterDefaults_stmt(self, ctx:IceToolToolinParser.Defaults_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDefaults_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#defaults_stmt.
	def exitDefaults_stmt(self, ctx:IceToolToolinParser.Defaults_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDefaults_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#defaults_ops.
	def enterDefaults_ops(self, ctx:IceToolToolinParser.Defaults_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDefaults_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#defaults_ops.
	def exitDefaults_ops(self, ctx:IceToolToolinParser.Defaults_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDefaults_ops")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#display_stmt.
	def enterDisplay_stmt(self, ctx:IceToolToolinParser.Display_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDisplay_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#display_stmt.
	def exitDisplay_stmt(self, ctx:IceToolToolinParser.Display_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDisplay_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#display_ops.
	def enterDisplay_ops(self, ctx:IceToolToolinParser.Display_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDisplay_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#display_ops.
	def exitDisplay_ops(self, ctx:IceToolToolinParser.Display_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDisplay_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#merge_stmt.
	def enterMerge_stmt(self, ctx:IceToolToolinParser.Merge_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterMerge_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#merge_stmt.
	def exitMerge_stmt(self, ctx:IceToolToolinParser.Merge_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitMerge_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#merge_ops.
	def enterMerge_ops(self, ctx:IceToolToolinParser.Merge_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterMerge_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#merge_ops.
	def exitMerge_ops(self, ctx:IceToolToolinParser.Merge_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitMerge_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#mode_stmt.
	def enterMode_stmt(self, ctx:IceToolToolinParser.Mode_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterMode_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#mode_stmt.
	def exitMode_stmt(self, ctx:IceToolToolinParser.Mode_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitMode_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#occur_stmt.
	def enterOccur_stmt(self, ctx:IceToolToolinParser.Occur_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOccur_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#occur_stmt.
	def exitOccur_stmt(self, ctx:IceToolToolinParser.Occur_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOccur_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#occur_ops.
	def enterOccur_ops(self, ctx:IceToolToolinParser.Occur_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOccur_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#occur_ops.
	def exitOccur_ops(self, ctx:IceToolToolinParser.Occur_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOccur_ops")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#occur_opt.
	def enterOccur_opt(self, ctx:IceToolToolinParser.Occur_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOccur_opt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#occur_opt.
	def exitOccur_opt(self, ctx:IceToolToolinParser.Occur_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOccur_opt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#occur_list_op.
	def enterOccur_list_op(self, ctx:IceToolToolinParser.Occur_list_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOccur_list_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#occur_list_op.
	def exitOccur_list_op(self, ctx:IceToolToolinParser.Occur_list_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOccur_list_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#range_stmt.
	def enterRange_stmt(self, ctx:IceToolToolinParser.Range_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRange_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#range_stmt.
	def exitRange_stmt(self, ctx:IceToolToolinParser.Range_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRange_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#range_ops.
	def enterRange_ops(self, ctx:IceToolToolinParser.Range_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRange_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#range_ops.
	def exitRange_ops(self, ctx:IceToolToolinParser.Range_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRange_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#range_opt.
	def enterRange_opt(self, ctx:IceToolToolinParser.Range_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRange_opt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#range_opt.
	def exitRange_opt(self, ctx:IceToolToolinParser.Range_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRange_opt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#resize_stmt.
	def enterResize_stmt(self, ctx:IceToolToolinParser.Resize_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterResize_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#resize_stmt.
	def exitResize_stmt(self, ctx:IceToolToolinParser.Resize_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitResize_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#resize_ops.
	def enterResize_ops(self, ctx:IceToolToolinParser.Resize_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterResize_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#resize_ops.
	def exitResize_ops(self, ctx:IceToolToolinParser.Resize_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitResize_ops")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#select_stmt.
	def enterSelect_stmt(self, ctx:IceToolToolinParser.Select_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#select_stmt.
	def exitSelect_stmt(self, ctx:IceToolToolinParser.Select_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#select_opt.
	def enterSelect_opt(self, ctx:IceToolToolinParser.Select_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_opt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#select_opt.
	def exitSelect_opt(self, ctx:IceToolToolinParser.Select_optContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_opt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#select_fmt.
	def enterSelect_fmt(self, ctx:IceToolToolinParser.Select_fmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSelect_fmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#select_fmt.
	def exitSelect_fmt(self, ctx:IceToolToolinParser.Select_fmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSelect_fmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#sort_stmt.
	def enterSort_stmt(self, ctx:IceToolToolinParser.Sort_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#sort_stmt.
	def exitSort_stmt(self, ctx:IceToolToolinParser.Sort_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#sort_ops.
	def enterSort_ops(self, ctx:IceToolToolinParser.Sort_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSort_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#sort_ops.
	def exitSort_ops(self, ctx:IceToolToolinParser.Sort_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSort_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#splice_stmt.
	def enterSplice_stmt(self, ctx:IceToolToolinParser.Splice_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSplice_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#splice_stmt.
	def exitSplice_stmt(self, ctx:IceToolToolinParser.Splice_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSplice_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#splice_ops.
	def enterSplice_ops(self, ctx:IceToolToolinParser.Splice_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSplice_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#splice_ops.
	def exitSplice_ops(self, ctx:IceToolToolinParser.Splice_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSplice_ops")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#splice_opts.
	def enterSplice_opts(self, ctx:IceToolToolinParser.Splice_optsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSplice_opts")
		pass

	# Exit a parse tree produced by IceToolToolinParser#splice_opts.
	def exitSplice_opts(self, ctx:IceToolToolinParser.Splice_optsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSplice_opts")
		pass


	# Enter a parse tree produced by IceToolToolinParser#stats_stmt.
	def enterStats_stmt(self, ctx:IceToolToolinParser.Stats_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterStats_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#stats_stmt.
	def exitStats_stmt(self, ctx:IceToolToolinParser.Stats_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitStats_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#stats_ops.
	def enterStats_ops(self, ctx:IceToolToolinParser.Stats_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterStats_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#stats_ops.
	def exitStats_ops(self, ctx:IceToolToolinParser.Stats_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitStats_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#subset_stmt.
	def enterSubset_stmt(self, ctx:IceToolToolinParser.Subset_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSubset_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#subset_stmt.
	def exitSubset_stmt(self, ctx:IceToolToolinParser.Subset_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSubset_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#subset_ops.
	def enterSubset_ops(self, ctx:IceToolToolinParser.Subset_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSubset_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#subset_ops.
	def exitSubset_ops(self, ctx:IceToolToolinParser.Subset_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSubset_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#subset_opts.
	def enterSubset_opts(self, ctx:IceToolToolinParser.Subset_optsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSubset_opts")
		pass

	# Exit a parse tree produced by IceToolToolinParser#subset_opts.
	def exitSubset_opts(self, ctx:IceToolToolinParser.Subset_optsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSubset_opts")
		pass


	# Enter a parse tree produced by IceToolToolinParser#unique_stmt.
	def enterUnique_stmt(self, ctx:IceToolToolinParser.Unique_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterUnique_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#unique_stmt.
	def exitUnique_stmt(self, ctx:IceToolToolinParser.Unique_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitUnique_stmt")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#unique_ops.
	def enterUnique_ops(self, ctx:IceToolToolinParser.Unique_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterUnique_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#unique_ops.
	def exitUnique_ops(self, ctx:IceToolToolinParser.Unique_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitUnique_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#verify_stmt.
	def enterVerify_stmt(self, ctx:IceToolToolinParser.Verify_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterVerify_stmt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#verify_stmt.
	def exitVerify_stmt(self, ctx:IceToolToolinParser.Verify_stmtContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitVerify_stmt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#verify_ops.
	def enterVerify_ops(self, ctx:IceToolToolinParser.Verify_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterVerify_ops")
		pass

	# Exit a parse tree produced by IceToolToolinParser#verify_ops.
	def exitVerify_ops(self, ctx:IceToolToolinParser.Verify_opsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitVerify_ops")
		pass


	# Enter a parse tree produced by IceToolToolinParser#using_op.
	def enterUsing_op(self, ctx:IceToolToolinParser.Using_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterUsing_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#using_op.
	def exitUsing_op(self, ctx:IceToolToolinParser.Using_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitUsing_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#list_op.
	def enterList_op(self, ctx:IceToolToolinParser.List_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterList_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#list_op.
	def exitList_op(self, ctx:IceToolToolinParser.List_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitList_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#write_op.
	def enterWrite_op(self, ctx:IceToolToolinParser.Write_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterWrite_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#write_op.
	def exitWrite_op(self, ctx:IceToolToolinParser.Write_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitWrite_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#discard_op.
	def enterDiscard_op(self, ctx:IceToolToolinParser.Discard_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDiscard_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#discard_op.
	def exitDiscard_op(self, ctx:IceToolToolinParser.Discard_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDiscard_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#date_op.
	def enterDate_op(self, ctx:IceToolToolinParser.Date_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDate_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#date_op.
	def exitDate_op(self, ctx:IceToolToolinParser.Date_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDate_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#time_op.
	def enterTime_op(self, ctx:IceToolToolinParser.Time_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTime_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#time_op.
	def exitTime_op(self, ctx:IceToolToolinParser.Time_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTime_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#to_op.
	def enterTo_op(self, ctx:IceToolToolinParser.To_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTo_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#to_op.
	def exitTo_op(self, ctx:IceToolToolinParser.To_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTo_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#to_op_multi.
	def enterTo_op_multi(self, ctx:IceToolToolinParser.To_op_multiContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTo_op_multi")
		pass

	# Exit a parse tree produced by IceToolToolinParser#to_op_multi.
	def exitTo_op_multi(self, ctx:IceToolToolinParser.To_op_multiContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTo_op_multi")
		pass


	# Enter a parse tree produced by IceToolToolinParser#from_op.
	def enterFrom_op(self, ctx:IceToolToolinParser.From_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterFrom_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#from_op.
	def exitFrom_op(self, ctx:IceToolToolinParser.From_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitFrom_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#from_op_multi.
	def enterFrom_op_multi(self, ctx:IceToolToolinParser.From_op_multiContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterFrom_op_multi")
		pass

	# Exit a parse tree produced by IceToolToolinParser#from_op_multi.
	def exitFrom_op_multi(self, ctx:IceToolToolinParser.From_op_multiContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitFrom_op_multi")
		pass


	# Enter a parse tree produced by IceToolToolinParser#total_op.
	def enterTotal_op(self, ctx:IceToolToolinParser.Total_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTotal_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#total_op.
	def exitTotal_op(self, ctx:IceToolToolinParser.Total_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTotal_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#maximum_op.
	def enterMaximum_op(self, ctx:IceToolToolinParser.Maximum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterMaximum_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#maximum_op.
	def exitMaximum_op(self, ctx:IceToolToolinParser.Maximum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitMaximum_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#minimum_op.
	def enterMinimum_op(self, ctx:IceToolToolinParser.Minimum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterMinimum_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#minimum_op.
	def exitMinimum_op(self, ctx:IceToolToolinParser.Minimum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitMinimum_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#average_op.
	def enterAverage_op(self, ctx:IceToolToolinParser.Average_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterAverage_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#average_op.
	def exitAverage_op(self, ctx:IceToolToolinParser.Average_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitAverage_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#count_op.
	def enterCount_op(self, ctx:IceToolToolinParser.Count_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCount_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#count_op.
	def exitCount_op(self, ctx:IceToolToolinParser.Count_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCount_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#btitle_op.
	def enterBtitle_op(self, ctx:IceToolToolinParser.Btitle_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBtitle_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#btitle_op.
	def exitBtitle_op(self, ctx:IceToolToolinParser.Btitle_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBtitle_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#btotal_op.
	def enterBtotal_op(self, ctx:IceToolToolinParser.Btotal_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBtotal_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#btotal_op.
	def exitBtotal_op(self, ctx:IceToolToolinParser.Btotal_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBtotal_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#bmaximum_op.
	def enterBmaximum_op(self, ctx:IceToolToolinParser.Bmaximum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBmaximum_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#bmaximum_op.
	def exitBmaximum_op(self, ctx:IceToolToolinParser.Bmaximum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBmaximum_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#bminimum_op.
	def enterBminimum_op(self, ctx:IceToolToolinParser.Bminimum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBminimum_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#bminimum_op.
	def exitBminimum_op(self, ctx:IceToolToolinParser.Bminimum_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBminimum_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#baverage_op.
	def enterBaverage_op(self, ctx:IceToolToolinParser.Baverage_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBaverage_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#baverage_op.
	def exitBaverage_op(self, ctx:IceToolToolinParser.Baverage_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBaverage_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#bcount_op.
	def enterBcount_op(self, ctx:IceToolToolinParser.Bcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBcount_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#bcount_op.
	def exitBcount_op(self, ctx:IceToolToolinParser.Bcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBcount_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#text_op.
	def enterText_op(self, ctx:IceToolToolinParser.Text_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterText_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#text_op.
	def exitText_op(self, ctx:IceToolToolinParser.Text_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitText_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#limit_op.
	def enterLimit_op(self, ctx:IceToolToolinParser.Limit_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterLimit_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#limit_op.
	def exitLimit_op(self, ctx:IceToolToolinParser.Limit_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitLimit_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#indent_op.
	def enterIndent_op(self, ctx:IceToolToolinParser.Indent_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterIndent_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#indent_op.
	def exitIndent_op(self, ctx:IceToolToolinParser.Indent_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitIndent_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#lines_op.
	def enterLines_op(self, ctx:IceToolToolinParser.Lines_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterLines_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#lines_op.
	def exitLines_op(self, ctx:IceToolToolinParser.Lines_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitLines_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#width_op.
	def enterWidth_op(self, ctx:IceToolToolinParser.Width_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterWidth_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#width_op.
	def exitWidth_op(self, ctx:IceToolToolinParser.Width_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitWidth_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#between_op.
	def enterBetween_op(self, ctx:IceToolToolinParser.Between_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBetween_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#between_op.
	def exitBetween_op(self, ctx:IceToolToolinParser.Between_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBetween_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#tbetween_op.
	def enterTbetween_op(self, ctx:IceToolToolinParser.Tbetween_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTbetween_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#tbetween_op.
	def exitTbetween_op(self, ctx:IceToolToolinParser.Tbetween_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTbetween_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#to_len_op.
	def enterTo_len_op(self, ctx:IceToolToolinParser.To_len_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTo_len_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#to_len_op.
	def exitTo_len_op(self, ctx:IceToolToolinParser.To_len_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTo_len_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#on_op.
	def enterOn_op(self, ctx:IceToolToolinParser.On_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOn_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#on_op.
	def exitOn_op(self, ctx:IceToolToolinParser.On_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOn_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#disp_on_op.
	def enterDisp_on_op(self, ctx:IceToolToolinParser.Disp_on_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDisp_on_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#disp_on_op.
	def exitDisp_on_op(self, ctx:IceToolToolinParser.Disp_on_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDisp_on_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#occur_on_op.
	def enterOccur_on_op(self, ctx:IceToolToolinParser.Occur_on_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterOccur_on_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#occur_on_op.
	def exitOccur_on_op(self, ctx:IceToolToolinParser.Occur_on_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitOccur_on_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#vstype_op.
	def enterVstype_op(self, ctx:IceToolToolinParser.Vstype_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterVstype_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#vstype_op.
	def exitVstype_op(self, ctx:IceToolToolinParser.Vstype_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitVstype_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#locale_op.
	def enterLocale_op(self, ctx:IceToolToolinParser.Locale_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterLocale_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#locale_op.
	def exitLocale_op(self, ctx:IceToolToolinParser.Locale_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitLocale_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#break_op.
	def enterBreak_op(self, ctx:IceToolToolinParser.Break_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBreak_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#break_op.
	def exitBreak_op(self, ctx:IceToolToolinParser.Break_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBreak_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#edcount_op.
	def enterEdcount_op(self, ctx:IceToolToolinParser.Edcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterEdcount_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#edcount_op.
	def exitEdcount_op(self, ctx:IceToolToolinParser.Edcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitEdcount_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#edbcount_op.
	def enterEdbcount_op(self, ctx:IceToolToolinParser.Edbcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterEdbcount_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#edbcount_op.
	def exitEdbcount_op(self, ctx:IceToolToolinParser.Edbcount_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitEdbcount_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#title_op.
	def enterTitle_op(self, ctx:IceToolToolinParser.Title_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTitle_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#title_op.
	def exitTitle_op(self, ctx:IceToolToolinParser.Title_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTitle_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#header_op.
	def enterHeader_op(self, ctx:IceToolToolinParser.Header_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterHeader_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#header_op.
	def exitHeader_op(self, ctx:IceToolToolinParser.Header_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitHeader_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#header_op_ds.
	def enterHeader_op_ds(self, ctx:IceToolToolinParser.Header_op_dsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterHeader_op_ds")
		pass

	# Exit a parse tree produced by IceToolToolinParser#header_op_ds.
	def exitHeader_op_ds(self, ctx:IceToolToolinParser.Header_op_dsContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitHeader_op_ds")
		pass


	# Enter a parse tree produced by IceToolToolinParser#trailer_op.
	def enterTrailer_op(self, ctx:IceToolToolinParser.Trailer_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTrailer_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#trailer_op.
	def exitTrailer_op(self, ctx:IceToolToolinParser.Trailer_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTrailer_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#collkey_op.
	def enterCollkey_op(self, ctx:IceToolToolinParser.Collkey_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCollkey_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#collkey_op.
	def exitCollkey_op(self, ctx:IceToolToolinParser.Collkey_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCollkey_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#l_string.
	def enterL_string(self, ctx:IceToolToolinParser.L_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterL_string")
		pass

	# Exit a parse tree produced by IceToolToolinParser#l_string.
	def exitL_string(self, ctx:IceToolToolinParser.L_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitL_string")
		pass


	# Enter a parse tree produced by IceToolToolinParser#f_string.
	def enterF_string(self, ctx:IceToolToolinParser.F_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterF_string")
		pass

	# Exit a parse tree produced by IceToolToolinParser#f_string.
	def exitF_string(self, ctx:IceToolToolinParser.F_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitF_string")
		pass


	# Enter a parse tree produced by IceToolToolinParser#t_string.
	def enterT_string(self, ctx:IceToolToolinParser.T_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterT_string")
		pass

	# Exit a parse tree produced by IceToolToolinParser#t_string.
	def exitT_string(self, ctx:IceToolToolinParser.T_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitT_string")
		pass


	# Enter a parse tree produced by IceToolToolinParser#e_string.
	def enterE_string(self, ctx:IceToolToolinParser.E_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterE_string")
		pass

	# Exit a parse tree produced by IceToolToolinParser#e_string.
	def exitE_string(self, ctx:IceToolToolinParser.E_stringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitE_string")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#uzero_op.
	def enterUzero_op(self, ctx:IceToolToolinParser.Uzero_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterUzero_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#uzero_op.
	def exitUzero_op(self, ctx:IceToolToolinParser.Uzero_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitUzero_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#serial_op.
	def enterSerial_op(self, ctx:IceToolToolinParser.Serial_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSerial_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#serial_op.
	def exitSerial_op(self, ctx:IceToolToolinParser.Serial_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSerial_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#jkfrom_op.
	def enterJkfrom_op(self, ctx:IceToolToolinParser.Jkfrom_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterJkfrom_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#jkfrom_op.
	def exitJkfrom_op(self, ctx:IceToolToolinParser.Jkfrom_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitJkfrom_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#statleft_op.
	def enterStatleft_op(self, ctx:IceToolToolinParser.Statleft_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterStatleft_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#statleft_op.
	def exitStatleft_op(self, ctx:IceToolToolinParser.Statleft_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitStatleft_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#listsdb_op.
	def enterListsdb_op(self, ctx:IceToolToolinParser.Listsdb_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterListsdb_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#listsdb_op.
	def exitListsdb_op(self, ctx:IceToolToolinParser.Listsdb_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitListsdb_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#tleft_op.
	def enterTleft_op(self, ctx:IceToolToolinParser.Tleft_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTleft_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#tleft_op.
	def exitTleft_op(self, ctx:IceToolToolinParser.Tleft_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTleft_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#tfirst_op.
	def enterTfirst_op(self, ctx:IceToolToolinParser.Tfirst_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterTfirst_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#tfirst_op.
	def exitTfirst_op(self, ctx:IceToolToolinParser.Tfirst_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitTfirst_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#page_op.
	def enterPage_op(self, ctx:IceToolToolinParser.Page_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterPage_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#page_op.
	def exitPage_op(self, ctx:IceToolToolinParser.Page_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitPage_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#nocc_op.
	def enterNocc_op(self, ctx:IceToolToolinParser.Nocc_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterNocc_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#nocc_op.
	def exitNocc_op(self, ctx:IceToolToolinParser.Nocc_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitNocc_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#longline_op.
	def enterLongline_op(self, ctx:IceToolToolinParser.Longline_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterLongline_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#longline_op.
	def exitLongline_op(self, ctx:IceToolToolinParser.Longline_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitLongline_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#nosign_op.
	def enterNosign_op(self, ctx:IceToolToolinParser.Nosign_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterNosign_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#nosign_op.
	def exitNosign_op(self, ctx:IceToolToolinParser.Nosign_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitNosign_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#n_dd.
	def enterN_dd(self, ctx:IceToolToolinParser.N_ddContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterN_dd")
		pass

	# Exit a parse tree produced by IceToolToolinParser#n_dd.
	def exitN_dd(self, ctx:IceToolToolinParser.N_ddContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitN_dd")
		pass


	# Enter a parse tree produced by IceToolToolinParser#u_dd.
	def enterU_dd(self, ctx:IceToolToolinParser.U_ddContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterU_dd")
		pass

	# Exit a parse tree produced by IceToolToolinParser#u_dd.
	def exitU_dd(self, ctx:IceToolToolinParser.U_ddContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitU_dd")
		pass


	# Enter a parse tree produced by IceToolToolinParser#slash_x.
	def enterSlash_x(self, ctx:IceToolToolinParser.Slash_xContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterSlash_x")
		pass

	# Exit a parse tree produced by IceToolToolinParser#slash_x.
	def exitSlash_x(self, ctx:IceToolToolinParser.Slash_xContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitSlash_x")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#vsam_code.
	def enterVsam_code(self, ctx:IceToolToolinParser.Vsam_codeContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterVsam_code")
		pass

	# Exit a parse tree produced by IceToolToolinParser#vsam_code.
	def exitVsam_code(self, ctx:IceToolToolinParser.Vsam_codeContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitVsam_code")
		pass


	# Enter a parse tree produced by IceToolToolinParser#collkey_type.
	def enterCollkey_type(self, ctx:IceToolToolinParser.Collkey_typeContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterCollkey_type")
		pass

	# Exit a parse tree produced by IceToolToolinParser#collkey_type.
	def exitCollkey_type(self, ctx:IceToolToolinParser.Collkey_typeContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitCollkey_type")
		pass


	# Enter a parse tree produced by IceToolToolinParser#rc_op.
	def enterRc_op(self, ctx:IceToolToolinParser.Rc_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRc_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#rc_op.
	def exitRc_op(self, ctx:IceToolToolinParser.Rc_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRc_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#blank_plus_op.
	def enterBlank_plus_op(self, ctx:IceToolToolinParser.Blank_plus_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterBlank_plus_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#blank_plus_op.
	def exitBlank_plus_op(self, ctx:IceToolToolinParser.Blank_plus_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitBlank_plus_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#formatting.
	def enterFormatting(self, ctx:IceToolToolinParser.FormattingContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterFormatting")
		pass

	# Exit a parse tree produced by IceToolToolinParser#formatting.
	def exitFormatting(self, ctx:IceToolToolinParser.FormattingContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitFormatting")
		pass


	# Enter a parse tree produced by IceToolToolinParser#formatt.
	def enterFormatt(self, ctx:IceToolToolinParser.FormattContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterFormatt")
		pass

	# Exit a parse tree produced by IceToolToolinParser#formatt.
	def exitFormatt(self, ctx:IceToolToolinParser.FormattContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitFormatt")
		pass


	# Enter a parse tree produced by IceToolToolinParser#with_op.
	def enterWith_op(self, ctx:IceToolToolinParser.With_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterWith_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#with_op.
	def exitWith_op(self, ctx:IceToolToolinParser.With_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitWith_op")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#rrn_op.
	def enterRrn_op(self, ctx:IceToolToolinParser.Rrn_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRrn_op")
		pass

	# Exit a parse tree produced by IceToolToolinParser#rrn_op.
	def exitRrn_op(self, ctx:IceToolToolinParser.Rrn_opContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRrn_op")
		pass


	# Enter a parse tree produced by IceToolToolinParser#ucannn_l_r_v.
	def enterUcannn_l_r_v(self, ctx:IceToolToolinParser.Ucannn_l_r_vContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterUcannn_l_r_v")
		pass

	# Exit a parse tree produced by IceToolToolinParser#ucannn_l_r_v.
	def exitUcannn_l_r_v(self, ctx:IceToolToolinParser.Ucannn_l_r_vContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitUcannn_l_r_v")
		pass


	# Enter a parse tree produced by IceToolToolinParser#name.
	def enterName(self, ctx:IceToolToolinParser.NameContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterName")
		pass

	# Exit a parse tree produced by IceToolToolinParser#name.
	def exitName(self, ctx:IceToolToolinParser.NameContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitName")
		pass


	# Enter a parse tree produced by IceToolToolinParser#start_pos.
	def enterStart_pos(self, ctx:IceToolToolinParser.Start_posContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterStart_pos")
		pass

	# Exit a parse tree produced by IceToolToolinParser#start_pos.
	def exitStart_pos(self, ctx:IceToolToolinParser.Start_posContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitStart_pos")
		pass


	# Enter a parse tree produced by IceToolToolinParser#length.
	def enterLength(self, ctx:IceToolToolinParser.LengthContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterLength")
		pass

	# Exit a parse tree produced by IceToolToolinParser#length.
	def exitLength(self, ctx:IceToolToolinParser.LengthContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitLength")
		pass


	# Enter a parse tree produced by IceToolToolinParser#record_num.
	def enterRecord_num(self, ctx:IceToolToolinParser.Record_numContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterRecord_num")
		pass

	# Exit a parse tree produced by IceToolToolinParser#record_num.
	def exitRecord_num(self, ctx:IceToolToolinParser.Record_numContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitRecord_num")
		pass


	# Enter a parse tree produced by IceToolToolinParser#integer.
	def enterInteger(self, ctx:IceToolToolinParser.IntegerContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterInteger")
		pass

	# Exit a parse tree produced by IceToolToolinParser#integer.
	def exitInteger(self, ctx:IceToolToolinParser.IntegerContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitInteger")
		pass
		
	# Enter a parse tree produced by IceToolToolinParser#qstring.
	def enterQstring(self, ctx:IceToolToolinParser.QstringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterQstring")
		pass

	# Exit a parse tree produced by IceToolToolinParser#qstring.
	def exitQstring(self, ctx:IceToolToolinParser.QstringContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitQstring")
		pass


	# Enter a parse tree produced by IceToolToolinParser#ddname_token.
	def enterDdname_token(self, ctx:IceToolToolinParser.Ddname_tokenContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDdname_token")
		pass

	# Exit a parse tree produced by IceToolToolinParser#ddname_token.
	def exitDdname_token(self, ctx:IceToolToolinParser.Ddname_tokenContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDdname_token")
		pass


	# Enter a parse tree produced by IceToolToolinParser#ddname_tokens.
	def enterDdname_tokens(self, ctx:IceToolToolinParser.Ddname_tokensContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterDdname_tokens")
		pass

	# Exit a parse tree produced by IceToolToolinParser#ddname_tokens.
	def exitDdname_tokens(self, ctx:IceToolToolinParser.Ddname_tokensContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitDdname_tokens")
		pass


	# Enter a parse tree produced by IceToolToolinParser#ptoken.
	def enterPtoken(self, ctx:IceToolToolinParser.PtokenContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterPtoken")
		pass

	# Exit a parse tree produced by IceToolToolinParser#ptoken.
	def exitPtoken(self, ctx:IceToolToolinParser.PtokenContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitPtoken")
		pass


	# Enter a parse tree produced by IceToolToolinParser#comma.
	def enterComma(self, ctx:IceToolToolinParser.CommaContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... enterComma")
		pass

	# Exit a parse tree produced by IceToolToolinParser#comma.
	def exitComma(self, ctx:IceToolToolinParser.CommaContext):
		if eventTraceEnabled is 1:
			self._log.write("listener ... exitComma")
		pass